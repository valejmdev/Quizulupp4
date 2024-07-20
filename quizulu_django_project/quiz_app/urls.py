from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quiz-index'),
    path('gamemodes/', views.gamemodes, name='quiz-gamemodes'),
    path('multiple-gamemode/', views.multiplegamemode, name='quiz-multiple-gamemode'),
    path('free-gamemode/', views.freegamemode, name='quiz-free-gamemode'),
    path('picture-gamemode/', views.picturegamemode, name='quiz-picture-gamemode'),
    path('quiz-creator/', views.quiz_creator, name='quiz-creator'),
    path('success/', views.success, name='success'),
    # Add more URL patterns here
]