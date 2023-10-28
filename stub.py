import dataclasses
from bs4 import BeautifulSoup
from typing import Optional
from html.parser import HTMLParser
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter



@dataclasses.dataclass
class Question:
    question_id: int
    title: str
    short_description: Optional[str]


@dataclasses.dataclass
class QuestionAnswer:
    username: str
    user_points: int
    up_votes: int
    body_html: str


def get_question_answers(question: Question) -> list[QuestionAnswer]:
    # TODO: Josh
    ...


def get_search_results(term: str, site='stackoverflow.com') -> list[Question]:
    # TODO: Robert
    ...

def choose_question_list(questions: list[Question]):
    # TODO: Mitul

    user_input = 0
    value_is_valid = True

    print("Select a question list: ")



    while value_is_valid:
        for i in range(len(questions)):
            try:
                print(f"Type {i + 1} to fetch: {questions[i].title}")
            except Exception:
                ...

        try:
            user_input = int(input("Select question number: "))
            if user_input > len(questions) or 0 >= user_input:
                raise ValueError("Please enter a valid number")
            else:
                value_is_valid = False

        except ValueError as e:
            print("Please enter a valid number")

    question = questions[user_input-1]
    return question
class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

def display_answers(question: Question, answers: list[QuestionAnswer]):
    # TODO: Mitul
    print(f"Question: {question.title}\n")
    print("Below are the expert-contributed solutions:\n")
    for idx, answer in enumerate(answers, 1):
        print(f"{'-'*50}")
        print(f"\nSolution {idx}:")
        # html_filter = HTMLFilter()
        # html_filter.feed(answer.body_html)
        # print(html_filter.text)
        soup = BeautifulSoup(answer.body_html, 'html.parser')
        # Find all code blocks

        code_blocks = soup.find_all('code')
        # Apply syntax highlighting to each code block
        # print(code_blocks)

        for code_block in code_blocks:
            code = code_block.get_text()
            # print(code)
            try:
                # lexer = get_lexer_by_name(code_block, stripall=True)
                # formatter = HtmlFormatter(style='colorful')
                highlighted_code = highlight(code, PythonLexer(), TerminalFormatter())
                # print(highlighted_code)
                code_block.replace_with(BeautifulSoup(highlighted_code, 'html.parser'))
            except Exception:
                pass
        # Print or save the modified HTML content
        modified_html = str(soup.get_text())
        print(modified_html)

        # print(soup.get_text())
        print('-'*50)

answer = """
<h2>429 Too Many Requests</h2>
<p>The HTTP <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429" rel="nofollow noreferrer">429 Too Many Requests</a> response status code indicates that the user has sent too many requests in a given amount of time (&quot;rate limiting&quot;). The response representations SHOULD include details explaining the condition, and MAY include a <code>Retry-After</code> header indicating how long to wait before making a new request.</p>
<p>When a server is under attack or just receiving a very large number of requests from a single party, responding to each with a <strong><code>429</code></strong> status code will consume resources. Therefore, servers are not required to use the <code>429</code> status code; when limiting resource usage, it may be more appropriate to just drop connections, or take other steps.</p>
<p>However, when I took you code and executed the same test, I got the perfect result as follows:</p>
<ul>
<li><p>Code Block:</p>
<pre><code>  import requests

  query = &quot;selenium&quot;
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
  url = 'https://www.google.com/search?q=' + query
  res = requests.get(url, headers=headers)
  print(res)
</code></pre>
</li>
<li><p>Console Output:</p>
<pre><code>  &lt;Response [200]&gt;
</code></pre>
</li>
</ul>
<blockquote>
<p>You can find a relevant discussion in <a href="https://stackoverflow.com/questions/55979980/failed-to-load-resource-the-server-responded-with-a-status-of-429-too-many-req/55986553#55986553">Failed to load resource: the server responded with a status of 429 (Too Many Requests) and 404 (Not Found) with ChromeDriver Chrome through Selenium</a></p>
</blockquote>
"""

answers = [QuestionAnswer(body_html=answer, up_votes=0, user_points=0, username="")]
question = Question(question_id=28, short_description="abc", title="testing")
display_answers(question,answers)