from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

from models import Question, QuestionAnswer


def choose_question_list(questions: list[Question]) -> Question:
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


def display_answers(question: Question, answers: list[QuestionAnswer]):
    # TODO: Mitul
    print(f"Question: {question.title}\n")
    print("Below are the expert-contributed solutions:\n")
    for idx, answer in enumerate(answers, 1):
        print(f"{'-'*50}")
        print(f"\nSolution {idx}:")
        soup = BeautifulSoup(answer.body_html, 'html.parser')
        # Find all code blocks

        code_blocks = soup.find_all('code')
        # Apply syntax highlighting to each code block
        # print(code_blocks)

        for code_block in code_blocks:
            code = code_block.get_text()
            # print(code)
            try:
                highlighted_code = highlight(code, PythonLexer(), TerminalFormatter())
                code_block.replace_with(BeautifulSoup(highlighted_code, 'html.parser'))
            except Exception:
                pass
        # Print or save the modified HTML content
        modified_html = str(soup.get_text())
        print(modified_html)

        print('-'*50)

    input('Press enter to choose another question')
