from django.shortcuts import render, redirect
from .models import Quiz
from .forms import QuizForm

def index(request):
    return render(request, 'quiz_app/index.html')

def gamemodes(request):
    return render(request, 'quiz_app/gamemodes.html')

def multiplegamemode(request):
    return render(request, 'quiz_app/multiple-categories.html')

def freegamemode(request):
    return render(request, 'quiz_app/free-categories.html')

def picturegamemode(request):
    return render(request, 'quiz_app/picture-categories.html')

def quiz_creator(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # need to add the quiz list
    else:
        form = QuizForm()
    return render(request, 'quiz_app/quiz-creator.html', {'form': form})

def success(request):
    return render(request, 'quiz_app/success.html')