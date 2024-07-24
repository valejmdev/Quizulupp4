from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import Quiz, Questions
from .forms import QuizForm
import random


def index(request):
    return render(request, 'quiz_app/index.html')

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