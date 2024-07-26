from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
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
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)
    incorrect_answer1 = models.CharField(max_length=300)
    incorrect_answer2 = models.CharField(max_length=300)
    incorrect_answer3 = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.question_text
    

class UserQuizProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    current_question_index = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user} - {self.quiz}'