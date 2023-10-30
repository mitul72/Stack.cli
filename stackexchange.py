import dataclasses
from typing import Optional

from stackapi import StackAPI

from models import Question, QuestionAnswer


def get_question_answers(question: Question) -> list[QuestionAnswer]:
    # TODO: Josh

    # Initialize the StackAPI client for Stack Overflow
    SITE = StackAPI('stackoverflow')

    # Fetch the post using the `questions` endpoint
    post = SITE.fetch('questions/{0}/answers'.format(question.question_id), filter='withbody')

    # Check if the post exists
    if post['items']:
        question_answers = []

        # Assuming you have already fetched the post and have post['items']
        for item in post['items']:
            # Create a QuestionAnswer object and populate its attributes
            if 'reputation' in item['owner']:
                user_points = item['owner']['reputation']
            else:
                user_points = None

            question_answer = QuestionAnswer(
                username=item['owner']['display_name'],
                user_points=user_points,
                up_votes=item['score'],
                body_html=item['body'],
                accepted=item['is_accepted']
            )


            # Append the QuestionAnswer object to the list
            question_answers.append(question_answer)

    else:
        print('Post not found.')

    # sorted_question_answers = sorted(question_answers, key=lambda x: x.up_votes, reverse=True)
    sorted_question_answers = sorted(question_answers, key=lambda x: (x.accepted, x.up_votes), reverse=True)

    return sorted_question_answers
