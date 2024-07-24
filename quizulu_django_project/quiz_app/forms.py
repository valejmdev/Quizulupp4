from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'category', 'description']
        widgets = {
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
            ])
        }