import re
import pathlib
import time
from typing import Generator, Tuple, Iterator

import requests
import fake_useragent
from bs4 import BeautifulSoup

from stub import Question


QUESTION_ID_REGEX = re.compile(r'questions/(\d+)/')


def get_search_results(query: str, site='stackoverflow.com') -> list[Question]:
    search_engine = GoogleSearch()
    return search_engine.get_search_results(query, site=site)


class GoogleSearch:
    def __init__(self, rate_limit_per_min: int = 6):
        self.session = requests.Session()
        self.session.headers['User-Agent'] = fake_useragent.UserAgent().random
        self._rate_limit_per_min = rate_limit_per_min
        self._last_request_file = pathlib.Path(__file__).parent / '.lastGoogleRequest'

    def get_search_results(self, query: str, site: str = None) -> list[Question]:
        if site:
            query = f'site:{site} {query}'

        self._handle_pre_request_rate_limit()

        resp = self.session.get(
            'https://www.google.com/search',
            params={
                'q': query,
                'og': query,
            }
        )
        self._set_last_request_time()

        resp.raise_for_status()

        questions = []
        for link, title, desc in self._parse_results(resp.content):
            if question_match := QUESTION_ID_REGEX.findall(link):
                question_id = int(question_match[0])
                questions.append(Question(question_id=question_id, title=title, short_description=desc))

        return questions

    @staticmethod
    def _parse_results(html: bytes) -> Iterator[Tuple[str, str, str]]:
        soup = BeautifulSoup(html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            # Find link, title, description
            link = result.find('a', href=True)
            title = result.find('h3')
            description_box = result.find('div', {'style': '-webkit-line-clamp:2'})
            if description_box:
                description = description_box.text
                if link and title and description:
                    yield link['href'], title.text, description

    def _handle_pre_request_rate_limit(self):
        last_request_time = self._get_last_request_time()
        time_since_last_request = time.time() - last_request_time
        min_time_since_last_request = 60 / self._rate_limit_per_min

        delta = min_time_since_last_request - time_since_last_request

        # Still within allowed requests per minute
        if delta <= 0:
            return

        # If we can sleep for less than 5 seconds to avoid hitting the rate limit, do it. Otherwise, throw an exception
        if delta <= 5:
            time.sleep(delta)
        else:
            raise RuntimeError(f'Google search stopped to prevent rate limit being hit. '
                               f'Last request was {round(time_since_last_request, 3)} seconds ago.')

    def _get_last_request_time(self) -> float:
        try:
            return float(self._last_request_file.read_text())
        except (FileNotFoundError, TypeError, ValueError):
            return 0.0

    def _set_last_request_time(self):
        self._last_request_file.write_text(str(time.time()))
