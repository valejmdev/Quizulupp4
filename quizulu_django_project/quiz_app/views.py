from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the quiz index.")

def gamemodes(request):
    return HttpResponse("You are at the gamemodes page")