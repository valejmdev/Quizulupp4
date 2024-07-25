from django.urls import path
from . import views
from .views import (
    QuizUpdateView, QuizDeleteView, 
    QuestionUpdateView, QuestionDeleteView,
    QuestionCreateView, quiz_creator, success, 
    list_categories, random_quiz, quiz_detail
)

urlpatterns = [
    path('', views.index, name='quiz-index'),
    path('categories/', views.list_categories, name='categories'),
    path('quiz-creator/', views.quiz_creator, name='quiz-creator'),
    path('success/', views.success, name='success'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz-detail'),
    path('random_quiz/<str:category>/', views.random_quiz, name='random-quiz'),
    path('quiz/<int:pk>/questions/new/', views.QuestionCreateView.as_view(), name='question-creator'),
    path('quiz/<int:pk>/edit/', QuizUpdateView.as_view(), name='quiz-update'),
    path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete'),
    path('questions/<int:pk>/edit/', QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('my-quizzes/', views.my_quizzes, name='my-quizzes'),
    path('quiz/<int:quiz_id>/play/', views.play_quiz, name='play_quiz'),
]

