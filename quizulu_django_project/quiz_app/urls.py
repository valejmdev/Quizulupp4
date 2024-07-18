from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quiz-index'),
    path('gamemodes/', views.gamemodes, name='quiz-gamemodes'),
    # Add more URL patterns here
]