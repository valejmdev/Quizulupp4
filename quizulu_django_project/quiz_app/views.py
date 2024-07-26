from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Quiz, Questions
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

def play_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.questions_set.all()
    current_question = 0
    answers = []  # Define the answers variable here
    if request.method == 'POST':
        if 'next_question' in request.POST:
            current_question += 1
        elif 'submit_answer' in request.POST:
            # Check the answer and update the user's score
            pass
            answers = [questions[current_question].correct_answer, questions[current_question].answer1, questions[current_question].answer2, questions[current_question].answer3]
            random.shuffle(answers)
    else:
        answers = [questions[current_question].correct_answer, questions[current_question].answer1, questions[current_question].answer2, questions[current_question].answer3]
        random.shuffle(answers)
    return render(request, 'quiz_app/play_quiz.html', {'quiz': quiz, 'questions': questions, 'current_question': current_question, 'answers': answers})


@login_required
def my_quizzes(request):
    quizzes = Quiz.objects.filter(created_by=request.user)
    return render(request, 'quiz_app/my_quizzes.html', {'quizzes': quizzes})


@login_required
class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ['title', 'category', 'description']
    template_name = 'quiz_app/quiz_form.html'

    def form_valid(self, form):
        logging.info('Form is valid. Quiz is being updated.')
        return super().form_valid(form)

    def form_invalid(self, form):
        logging.error('Form is invalid. Errors: %s', form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.pk})


@login_required
class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz_app/quiz_confirm_delete.html'
    success_url = reverse_lazy('quiz-index')


@login_required
class QuestionUpdateView(UpdateView):
    model = Questions
    fields = ['question', 'correct_answer', 'answer1', 'answer2', 'answer3']
    template_name = 'quiz_app/question_form.html'

    def get_success_url(self):
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.quiz.pk})


@login_required
class QuestionDeleteView(DeleteView):
    model = Questions
    template_name = 'quiz_app/question_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.quiz.pk})

@login_required
def quiz_creator(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('question-creator', pk=quiz.pk)
    else:
        form = QuizForm()
    return render(request, 'quiz_app/quiz-creator.html', {'form': form})

def success(request):
    return render(request, 'quiz_app/success.html')

@login_required
class QuestionCreateView(CreateView):
    model = Questions
    fields = ['question', 'correct_answer', 'answer1', 'answer2', 'answer3']
    template_name = 'quiz_app/question_form.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['quiz'] = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        context['quiz'] = quiz
        context['questions_count'] = quiz.questions_set.count()
        return context

    def form_valid(self, form):
        form.instance.quiz_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question-creator', kwargs={'pk': self.kwargs['pk']})