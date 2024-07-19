from django.shortcuts import render

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

def quizcreator(request):
    return render(request, 'quiz_app/quiz-creator.html')
