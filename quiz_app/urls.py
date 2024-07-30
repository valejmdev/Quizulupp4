from django.urls import path
from . import views  

urlpatterns = [
    # Home page for the quiz application
    path('', views.index, name='quiz-index'),
    # Page to list all categories
    path('categories/', views.list_categories, name='categories'),
    # Page to create a new quiz
    path('quiz-creator/', views.MyQuizCreateView.as_view(), name='quiz-creator'),
    # Detail page for a specific quiz
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz-detail'),
    # Page to get a random quiz from a specific category
    path('random_quiz/<str:category>/', views.random_quiz, name='random-quiz'),
    # Page to create a new question for a specific quiz
    path('quiz/<int:pk>/questions/new/', views.QuestionCreateView.as_view(), name='question-creator'),
    # Page to edit a specific quiz
    path('quiz/<int:pk>/edit/', views.QuizUpdateView.as_view(), name='quiz-update'),
    # Page to delete a specific quiz
    path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz-delete'),
    # Page to view the user's quizzes
    path('my-quizzes/', views.my_quizzes, name='my-quizzes'),
    # Page to play a specific quiz
    path('quiz/<int:quiz_id>/play/', views.play_quiz, name='play_quiz'),
    # Page to view results of a specific quiz
    path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
    # Page to view the leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]