from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    gamemode = models.CharField(max_length=50, choices=[
        ('multipleChoice', 'Multiple Choice'),
        ('freeWriting', 'Free Writing'),
        ('withPictures', 'With Pictures')
    ])
    category = models.CharField(max_length=50, choices=[
        ('biology', 'Biology'),
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
        ('geography', 'Geography'),
        ('popMusic', 'Pop Music'),
        ('rockMusic', 'Rock Music'),
        ('electroMusic', 'Electro Music'),
        ('classicalMusic', 'Classical Music'),
        ('rapMusic', 'Rap Music'),
        ('movies', 'Movies'),
        ('tvShows', 'TV Shows'),
        ('literature', 'Literature'),
        ('animeManga', 'Anime & Manga'),
        ('computerScience', 'Computer Science'),
        ('videoGames', 'Video Games'),
        ('sports', 'Sports'),
        ('eSports', 'E-Sports'),
        ('languages', 'Languages'),
        ('history', 'History'),
        ('misc', 'Misc.')
    ])
    number_of_questions = models.IntegerField(choices=[(i, str(i)) for i in range(2, 11)])
    description = models.TextField()

    def __str__(self):
        return self.title


class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)
    answer1 = models.CharField(max_length=300)
    answer2 = models.CharField(max_length=300)
    answer3 = models.CharField(max_length=300)