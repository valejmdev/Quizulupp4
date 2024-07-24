from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quiz-index'),
    path('categories/', views.list_categories, name='categories'),
    path('quiz-creator/', views.quiz_creator, name='quiz-creator'),
    path('success/', views.success, name='success'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz-detail'),
    path('random_quiz/<str:category>/', views.random_quiz, name='random-quiz'),
    path('quiz/<int:pk>/questions/new/', views.QuestionCreateView.as_view(), name='question-creator'),

]

