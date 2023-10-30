import os
import sys

from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import guess_lexer, PythonLexer
from pygments.formatters import Terminal256Formatter
from pynput.keyboard import Key, Listener

from models import Question, QuestionAnswer


def choose_question_list(questions: list[Question]) -> Question:
    # TODO: Mitul

    user_input = 0
    value_is_valid = True

    print("Select a question list: ")

    num_keys = list(f"'{i}'" for i in range(0, 10))
    num_keys.append("'q'")
    for i in range(len(questions[:10])):
        print(f"Type {i} to fetch: {questions[i].title}")

    key = _wait_for_keypress(*num_keys)
    if key == "'q'":
        sys.exit()

    user_input = int(str(key).replace("'", ''))
    question = questions[user_input]
    return question


def display_answers(question: Question, answers: list[QuestionAnswer]):
    # TODO: Mitul
    print(f"Question: {question.title}\n")
    print("Below are the expert-contributed solutions:\n")

    index = 0

    while True:
        answer = answers[index]
        idx = index + 1

        print(f"{'-'*50}")
        print(f"\nSolution {idx}:")
        soup = BeautifulSoup(answer.body_html, 'html.parser')
        # Find all code blocks

        code_blocks = soup.find_all('code')
        # Apply syntax highlighting to each code block
        for code_block in code_blocks:
            code = code_block.get_text()
            guessLexer = guess_lexer(code)
            detected_lexer = guessLexer if guessLexer.name != "Text only" else PythonLexer()
            try:
                highlighted_code = highlight(code, detected_lexer, Terminal256Formatter(style="monokai"))
                code_block.replace_with(BeautifulSoup("\x1b[48;5;235m" + highlighted_code + "\x1b[0m", 'html.parser'))
            except Exception:
                pass
        # Print or save the modified HTML content
        modified_html = str(soup.get_text())
        print(modified_html)

        print('-'*5)

        key = _wait_for_keypress('Key.left', 'Key.right', "'q'")
        if key == 'Key.left':
            index -= 1
            if index < 0:
                index = len(answers) - 1
        if key == 'Key.right':
            index += 1
            if index >= len(answers):
                index = 0
        if key == "'q'":
            return
        clear_screen()

    input('Press enter to choose another question')



def _wait_for_keypress(*keys):
    pressed_key = [None]

    def on_press(key):
        if str(key) in keys:
            pressed_key[0] = str(key)
            return False

    with Listener(on_press=on_press) as listener:
        listener.join()

    return pressed_key[0]


def clear_screen():
    if sys.platform == 'win32':
        cmd = 'cls'
    else:
        cmd = 'clear'

    os.system(cmd)
