import argparse

import requests
from bs4 import BeautifulSoup as Soup


def google_search(query: str):
    resp = requests.get(
        'https://www.google.com/search',
        params={
            'q': query,
            'og': query
        }
    )
    if resp.status_code != 200:
        print(f'Google returned {resp.status_code}')
        return

    parser = Soup(resp.content)
    link = parser.select_one('a[href^="/url"]')
    if not link:
        print(f'Failed to locate link for {query}')
        return

    resp = requests.get('https://www.google.com' + link.get('href'))
    if resp.status_code != 200:
        print(f'Google returned {resp.status_code}')
        return

    parser = Soup(resp.content)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', default='stackoverflow', type=str)
    parser.add_argument('prompt', type=str, nargs='+')

    args = parser.parse_args()
    args.prompt = ' '.join(args.prompt)

    return args


if __name__ == '__main__':
    args = parse_args()

    print(args.prompt)
