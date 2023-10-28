import sys
import os
import argparse

import search
import display
import stackexchange


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', default='stackoverflow.com', type=str)
    parser.add_argument('prompt', type=str, nargs='+')

    args = parser.parse_args()
    args.prompt = ' '.join(args.prompt)

    return args


def main():
    args = parse_args()

    display.clear_screen()
    print(f'Running search: {args.prompt}')

    questions = search.get_search_results(args.prompt, site=args.site)
    if not questions:
        print('No results found', file=sys.stderr)
        return

    while True:
        display.clear_screen()
        question = display.choose_question_list(questions)
        answers = stackexchange.get_question_answers(question)

        display.clear_screen()
        display.display_answers(question, answers)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...
