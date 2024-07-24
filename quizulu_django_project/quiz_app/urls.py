from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quiz-index'),
    path('gamemodes/', views.gamemodes, name='quiz-gamemodes'),
    path('multiple-gamemode/', views.QuestionCreateView.as_view(), name='quiz-multiple-gamemode'),
    path('free-gamemode/', views.freegamemode, name='quiz-free-gamemode'),
    path('picture-gamemode/', views.picturegamemode, name='quiz-picture-gamemode'),
    path('quiz-creator/', views.quiz_creator, name='quiz-creator'),
    path('success/', views.success, name='success'),
    path('multiple-creator/', views.multiplecreator, name='quiz-multiple-creator'),
    path('free-creator/', views.freecreator, name='quiz-free-creator'),
    path('picture-creator/', views.picturecreator, name='quiz-picture-creator'),
    path('redirect-creator-mode/', views.redirect_creator_mode, name='redirect-creator-mode'),
    # Add more URL patterns here
]