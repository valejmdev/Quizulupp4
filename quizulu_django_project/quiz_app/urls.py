from django.urls import path
from . import views
from .views import (
    QuizCreateView,
    QuizUpdateView,
    QuizDeleteView,
    QuestionUpdateView,
    QuestionDeleteView,
    QuestionCreateView,
    list_categories,
    random_quiz,
    quiz_detail,
    my_quizzes,
    play_quiz,
    quiz_results
)

urlpatterns = [
        path('', views.index, name='quiz-index'),
    path('categories/', views.list_categories, name='categories'),
    path('quiz-creator/', views.QuizCreateView.as_view(), name='quiz-creator'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz-detail'),
    path('random_quiz/<str:category>/', random_quiz, name='random-quiz'),
    path('quiz/<int:pk>/questions/new/', views.QuestionCreateView.as_view(), name='question-creator'),
    path('quiz/<int:pk>/edit/', views.QuizUpdateView.as_view(), name='quiz-update'),
    path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz-delete'),
    path('questions/<int:pk>/edit/', views.QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('my-quizzes/', my_quizzes, name='my-quizzes'),
    path('quiz/<int:quiz_id>/play/', play_quiz, name='play_quiz'),
    path('quiz/<int:quiz_id>/results/', quiz_results, name='quiz_results'),
]