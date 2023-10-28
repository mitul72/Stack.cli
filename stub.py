import dataclasses
from typing import Optional


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

def display_answers(question: Question, answers: list[QuestionAnswer]):
    # TODO: Mitul
    ...

