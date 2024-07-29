from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    """
    Represents a quiz with a title, category, description, and creator.
    
    Attributes:
        title (str): The title of the quiz.
        category (str): The category of the quiz, chosen from predefined options.
        description (str): A detailed description of the quiz.
        created_by (User): The user who created the quiz.
    """
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('general', 'General Knowledge'),
        ('books', 'Entertainment: Books'),
        ('film', 'Entertainment: Film'),
        ('music', 'Entertainment: Music'),
        ('musicals', 'Entertainment: Musicals & Theatres'),
        ('television', 'Entertainment: Television'),
        ('videoGames', 'Entertainment: Video Games'),
        ('boardGames', 'Entertainment: Board Games'),
        ('nature', 'Science & Nature'),
        ('computers', 'Science: Computers'),
        ('mathematics', 'Science: Mathematics'),
        ('mythology', 'Mythology'),
        ('sports', 'Sports'),
        ('geography', 'Geography'),
        ('history', 'History'),
        ('politics', 'Politics'),
        ('art', 'Art'),
        ('celebrities', 'Celebrities'),
        ('animals', 'Animals'),
        ('vehicles', 'Vehicles'),
        ('comics', 'Entertainment: Comics'),
        ('gadgets', 'Science: Gadgets'),
        ('anime', 'Entertainment: Japanese Anime & Manga'),
        ('cartoons', 'Entertainment: Cartoon & Animations')
    ])
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """
        Return a string representation of the quiz, which is its title.
        """
        return self.title

class Question(models.Model):
    """
    Represents a question within a quiz, including the correct and incorrect answers.
    
    Attributes:
        quiz (Quiz): The quiz to which this question belongs.
        question_text (str): The text of the question.
        correct_answer (str): The correct answer to the question.
        incorrect_answer1 (str): The first incorrect answer option.
        incorrect_answer2 (str): The second incorrect answer option.
        incorrect_answer3 (str): The third incorrect answer option (optional).
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)
    incorrect_answer1 = models.CharField(max_length=300)
    incorrect_answer2 = models.CharField(max_length=300)
    incorrect_answer3 = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the question, which is its text.
        """
        return self.question_text
    

class UserQuizProgress(models.Model):
    """
    Tracks the progress of a user through a quiz, including their score and the current question index.
    
    Attributes:
        user (User): The user who is taking the quiz.
        quiz (Quiz): The quiz that the user is taking.
        score (int): The user's score in the quiz.
        current_question_index (int): The index of the current question in the quiz.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    current_question_index = models.IntegerField(default=0)
    
    def __str__(self):
        """
        Return a string representation of the user's progress in the quiz.
        """
        return f'{self.user} - {self.quiz}'