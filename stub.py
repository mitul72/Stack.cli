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
    accepted: bool


def get_question_answers(question: Question) -> list[QuestionAnswer]:
    # TODO: Josh
    ...


def get_search_results(term: str, site='stackoverflow.com') -> list[Question]:
    # TODO: Robert
    ...


def display_question_list(questions: list[Question]):
    # TODO: Mitul
    ...


def display_answers(question: Question, answers: list[QuestionAnswer]):
    # TODO: Mitul
    ...
