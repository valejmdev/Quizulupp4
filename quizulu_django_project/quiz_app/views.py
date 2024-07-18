from django.shortcuts import render

def index(request):
    return render(request, 'quiz_app/index.html')

def gamemodes(request):
    return render(request, 'quiz_app/gamemodes.html')