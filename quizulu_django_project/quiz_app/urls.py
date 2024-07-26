from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='quiz-index'),
    path('categories/', views.list_categories, name='categories'),
    path('quiz-creator/', views.MyQuizCreateView.as_view(), name='quiz-creator'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz-detail'),
    path('random_quiz/<str:category>/', views.random_quiz, name='random-quiz'),
    path('quiz/<int:pk>/questions/new/', views.QuestionCreateView.as_view(), name='question-creator'),
    path('quiz/<int:pk>/edit/', views.QuizUpdateView.as_view(), name='quiz-update'),
    path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz-delete'),
    path('questions/<int:pk>/edit/', views.QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('my-quizzes/', views.my_quizzes, name='my-quizzes'),
    path('quiz/<int:quiz_id>/play/', views.play_quiz, name='play_quiz'),
    path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
]