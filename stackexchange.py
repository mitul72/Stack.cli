import dataclasses
from typing import Optional

from stackapi import StackAPI

from stub import Question, QuestionAnswer


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
            question_answer = QuestionAnswer(
                username=item['owner']['display_name'],
                user_points=item['owner']['reputation'],
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


question = Question(question_id=56758333, title="Error 429 with simple query on google with requests python",
                    short_description="This is a sample description.")

question_answers = get_question_answers(question)

for question_answer in question_answers:
    print("Username:", question_answer.username)
    print("Accepted:", question_answer.accepted)
    print("User Points:", question_answer.user_points)
    print("Up Votes:", question_answer.up_votes)
    # print("Body HTML:", question_answer.body_html)
    print("---------------------------")

