from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    """
    A form for creating and updating Quiz instances.
    
    This form uses the `Quiz` model and includes fields for the quiz's title,
    category, and description. It also customizes the widget for the 'category'
    field to use a select dropdown with predefined choices.
    """
    class Meta:
        model = Quiz
        fields = ['title', 'category', 'description']
        widgets = {
            'category': forms.Select(choices=[
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
        }