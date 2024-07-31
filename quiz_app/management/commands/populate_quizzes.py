import time
import requests
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from quiz_app.models import Quiz, Question


class Command(BaseCommand):
    help = 'Populate the database with initial quiz data'

    def handle(self, *args, **kwargs):
        all_categories = [
            ('general', 9),
            ('books', 10),
            ('film', 11),
            ('music', 12),
            ('musicals', 13),
            ('television', 14),
            ('videoGames', 15),
            ('boardGames', 16),
            ('nature', 17),
            ('computers', 18),
            ('mathematics', 19),
            ('mythology', 20),
            ('sports', 21),
            ('geography', 22),
            ('history', 23),
            ('politics', 24),
            ('art', 25),
            ('celebrities', 26),
            ('animals', 27),
            ('vehicles', 28),
            ('comics', 29),
            ('gadgets', 30),
            ('anime', 31),
            ('cartoons', 32)
        ]

        # Split categories into batches
        batch_size = 5  # Number of categories per batch
        for i in range(0, len(all_categories), batch_size):
            categories = all_categories[i:i + batch_size]

            if not User.objects.exists():
                self.stdout.write(
                    self.style.ERROR(
                        'No users found. Create a user before running this.'
                    )
                )
                return

            user = User.objects.first()

            for category, category_id in categories:
                try:
                    self.stdout.write(
                        f'Fetching data for category: {category}'
                    )
                    response = requests.get(
                        f'https://opentdb.com/api.php?amount=10&category='
                        f'{category_id}&type=multiple'
                    )
                    self.stdout.write(f'Status Code: {response.status_code}')
                    self.stdout.write(f'Response Content: {response.text}')

                    if response.status_code == 429:
                        self.stdout.write(self.style.ERROR(
                            'Rate limit exceeded. Waiting before retrying.'
                        ))
                        time.sleep(60)  # Wait for 60 seconds before retrying
                        continue

                    if response.status_code != 200:
                        self.stdout.write(self.style.ERROR(
                            f'Failed to fetch data for category: {category}'
                        ))
                        continue

                    data = response.json()

                    if data.get('response_code') != 0:
                        self.stdout.write(self.style.ERROR(
                            f'Error in API response for category: {category}. '
                            f'Error: '
                            f'{data.get("response_message", "Unknown error")}.'
                        ))
                        continue

                    quiz = Quiz.objects.create(
                        title=f'{category.title()} Quiz',
                        category=category,
                        description=(
                            f'This quiz contains questions about '
                            f'{category.replace("_", " ")}.'
                        ),
                        created_by=user
                    )

                    for item in data.get('results', []):
                        Question.objects.create(
                            quiz=quiz,
                            question_text=item['question'],
                            correct_answer=item['correct_answer'],
                            incorrect_answer1=item['incorrect_answers'][0],
                            incorrect_answer2=item['incorrect_answers'][1],
                            incorrect_answer3=(
                                item['incorrect_answers'][2]
                                if len(item['incorrect_answers']) > 2
                                else None
                            )
                        )

                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Successfully populated quiz for category: '
                            f'{category}'
                        )
                    )

                except requests.RequestException as e:
                    self.stdout.write(self.style.ERROR(
                        f'Request exception for: {category}. Error: {e}'
                    ))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(
                        f'Unexpected error for: {category}. Error: {e}'
                    ))

            self.stdout.write(self.style.SUCCESS(
                'Batch completed. Waiting before starting the next batch.'
            ))
            time.sleep(30)  # Wait for 30 seconds before processing next batch
