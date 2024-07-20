from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'gamemode', 'category', 'number_of_questions', 'description']
        widgets = {
            'gamemode': forms.RadioSelect(choices=[
                ('multipleChoice', 'Multiple Choice'),
                ('freeWriting', 'Free Writing'),
                ('withPictures', 'With Pictures')
            ]),
            'category': forms.Select(choices=[
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
            ]),
            'number_of_questions': forms.Select(choices=[(i, str(i)) for i in range(2, 11)])
        }