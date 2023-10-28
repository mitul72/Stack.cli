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
