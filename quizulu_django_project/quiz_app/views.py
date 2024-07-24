from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quiz, Questions
from .forms import QuizForm
from django.views.generic.edit import CreateView

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

def multiplecreator(request):
    return render(request, 'quiz_app/multiple-creator.html')

def freecreator(request):
    return render(request, 'quiz_app/free-creator.html')

def picturecreator(request):
    return render(request, 'quiz_app/picture-creator.html')

def redirect_creator_mode(request):
    if request.method == 'POST':
        game_mode = request.POST.get('gamemode')
        if game_mode == 'multipleChoice':
            return redirect('quiz-multiple-creator')
        elif game_mode == 'freeWriting':
            return redirect('quiz-free-creator')
        elif game_mode == 'withPictures':
            return redirect('quiz-picture-creator')
    return redirect('quiz-creator')


class QuestionCreateView(CreateView):
    model = Questions
    fields = ['question']
        
