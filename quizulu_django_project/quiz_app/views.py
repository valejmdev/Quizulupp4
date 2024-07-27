from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Quiz, Question, UserQuizProgress
from .forms import QuizForm
import logging
import random

def index(request):
    return render(request, 'quiz_app/index.html')

def list_categories(request):
    categories = Quiz.objects.values_list('category', flat=True).distinct()
    return render(request, 'quiz_app/categories.html', {'categories': categories})

def random_quiz(request, category):
    quizzes = Quiz.objects.filter(category=category)
    if quizzes.exists():
        quiz = random.choice(quizzes)
        return redirect('quiz-detail', quiz_id=quiz.id)
    else:
        return render(request, 'quiz_app/no_quiz.html', {'category': category})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz})

@login_required
def play_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = list(quiz.question_set.all())

    if not questions:
        return render(request, 'quiz_app/empty_quiz.html', {'quiz': quiz})

    progress, created = UserQuizProgress.objects.get_or_create(user=request.user, quiz=quiz)
    current_question_index = progress.current_question_index if not created else 0

    if current_question_index >= len(questions):
        return redirect('quiz_results', quiz_id=quiz_id)

    current_question = questions[current_question_index]

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        
        if selected_answer:
            if selected_answer == current_question.correct_answer:
                progress.score += 1

            progress.current_question_index += 1

            if progress.current_question_index >= len(questions):
                progress.save()
                return redirect('quiz_results', quiz_id=quiz_id)
            else:
                progress.save()
                return redirect('play_quiz', quiz_id=quiz_id)

    answers = [current_question.correct_answer]
    if current_question.incorrect_answer1:
        answers.append(current_question.incorrect_answer1)
    if current_question.incorrect_answer2:
        answers.append(current_question.incorrect_answer2)
    if current_question.incorrect_answer3:
        answers.append(current_question.incorrect_answer3)

    random.shuffle(answers)

    context = {
        'quiz': quiz,
        'question': current_question.question_text,
        'answers': answers,
        'question_number': current_question_index + 1,
        'total_questions': len(questions),
    }
    return render(request, 'quiz_app/play_quiz.html', context)

@login_required
def quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    progress = get_object_or_404(UserQuizProgress, user=request.user, quiz=quiz)
    
    context = {
        'quiz': quiz,
        'score': progress.score,
        'total_questions': quiz.question_set.count(),
    }
    return render(request, 'quiz_app/quiz_results.html', context)

@login_required
def my_quizzes(request):
    quizzes = Quiz.objects.filter(created_by=request.user)
    return render(request, 'quiz_app/my_quizzes.html', {'quizzes': quizzes})

class MyQuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_app/quiz_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question-creator', kwargs={'pk': self.object.pk})

class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = Quiz
    fields = ['title', 'category', 'description']
    template_name = 'quiz_app/quiz_form.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this quiz.")
        return obj

    def get_success_url(self):
        return reverse_lazy('question-creator', kwargs={'pk': self.object.pk})

class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = Quiz
    template_name = 'quiz_app/quiz_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this quiz.")
        return obj

    def get_success_url(self):
        return reverse_lazy('quiz-index')

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['question', 'correct_answer', 'answer1', 'answer2', 'answer3']
    template_name = 'quiz_app/question_form.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.quiz.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this question.")
        return obj

    def get_success_url(self):
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.quiz.pk})

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'quiz_app/question_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.quiz.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this question.")
        return obj

    def get_success_url(self):
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.quiz.pk})

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_text', 'correct_answer', 'incorrect_answer1', 'incorrect_answer2', 'incorrect_answer3']
    template_name = 'quiz_app/question_form.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['quiz'] = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        context['quiz'] = quiz
        context['question_count'] = quiz.question_set.count()
        return context

    def form_valid(self, form):
        form.instance.quiz_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question-creator', kwargs={'pk': self.kwargs['pk']})