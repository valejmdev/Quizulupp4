from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.contrib import messages
from .models import Quiz, Question, UserQuizProgress
from .forms import QuizForm
import random

def index(request):
    """
    Render the home page of the quiz application.
    """
    return render(request, 'quiz_app/index.html')

def list_categories(request):
    """
    Render a page listing all distinct quiz categories.
    """
    categories = Quiz.objects.values_list('category', flat=True).distinct()
    return render(request, 'quiz_app/categories.html', {'categories': categories})

def random_quiz(request, category):
    """
    Redirect to a random quiz from the specified category, or render a page if no quizzes are available.
    
    Args:
        category (str): The category of the quiz to be selected.
    """
    quizzes = Quiz.objects.filter(category=category)
    if quizzes.exists():
        quiz = random.choice(quizzes)
        return redirect('quiz-detail', quiz_id=quiz.id)
    else:
        return render(request, 'quiz_app/no_quiz.html', {'category': category})

def quiz_detail(request, quiz_id):
    """
    Render a page showing details of a specific quiz.
    
    Args:
        quiz_id (int): The ID of the quiz to be displayed.
    """
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz})

@login_required
def play_quiz(request, quiz_id):
    """
    Handle the logic for playing a quiz, including question progression and answer checking.
    
    Args:
        quiz_id (int): The ID of the quiz to be played.
    """
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
    """
    Render the results page for a completed quiz, showing the user's score.
    
    Args:
        quiz_id (int): The ID of the quiz whose results are to be displayed.
    """
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
    """
    Render a page showing all quizzes created by the logged-in user.
    """
    quizzes = Quiz.objects.filter(created_by=request.user)
    return render(request, 'quiz_app/my_quizzes.html', {'quizzes': quizzes})

class MyQuizCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new quiz. Only accessible to logged-in users.
    """
    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_app/quiz_form.html'

    def form_valid(self, form):
        """
        Assign the current user as the creator of the quiz and redirect to the question creation page.
        """
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return HttpResponseRedirect(reverse('question-creator', kwargs={'pk': self.object.pk}))

    def get_success_url(self):
        """
        Redirect to the 'my-quizzes' page upon successful form submission.
        """
        return reverse_lazy('my-quizzes')

class QuizUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing quiz. Only accessible to the creator of the quiz.
    """
    model = Quiz
    fields = ['title', 'category', 'description']
    template_name = 'quiz_app/quiz_form.html'

    def get_object(self, queryset=None):
        """
        Ensure that only the creator of the quiz can update it.
        """
        obj = super().get_object(queryset)
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this quiz.")
        return obj

    def form_valid(self, form):
        """
        Show a success message upon successful form submission.
        """
        messages.success(self.request, 'Quiz updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the 'my-quizzes' page upon successful form submission.
        """
        return reverse_lazy('my-quizzes')

class QuizDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a quiz. Only accessible to the creator of the quiz.
    """
    model = Quiz
    template_name = 'quiz_app/quiz_confirm_delete.html'

    def get_object(self, queryset=None):
        """
        Ensure that only the creator of the quiz can delete it.
        """
        obj = super().get_object(queryset)
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this quiz.")
        return obj

    def get_success_url(self):
        """
        Redirect to the home page upon successful deletion of the quiz.
        """
        return reverse_lazy('quiz-index')

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a question. Only accessible to the creator of the quiz to which the question belongs.
    """
    model = Question
    fields = ['question_text', 'correct_answer', 'incorrect_answer1', 'incorrect_answer2', 'incorrect_answer3']
    template_name = 'quiz_app/question_form.html'

    def get_object(self, queryset=None):
        """
        Ensure that only the creator of the quiz can update the question.
        """
        obj = super().get_object(queryset)
        if obj.quiz.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this question.")
        return obj

    def get_success_url(self):
        """
        Redirect to the detail page of the quiz to which the question belongs upon successful form submission.
        """
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.quiz.pk})

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a question. Only accessible to the creator of the quiz to which the question belongs.
    """
    model = Question
    template_name = 'quiz_app/question_confirm_delete.html'

    def get_object(self, queryset=None):
        """
        Ensure that only the creator of the quiz can delete the question.
        """
        obj = super().get_object(queryset)
        if obj.quiz.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this question.")
        return obj

    def get_success_url(self):
        """
        Redirect to the detail page of the quiz to which the question belongs upon successful deletion.
        """
        return reverse_lazy('quiz-detail', kwargs={'quiz_id': self.object.quiz.pk})

class QuestionCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new question for a specific quiz. Only accessible to logged-in users.
    """
    model = Question
    fields = ['question_text', 'correct_answer', 'incorrect_answer1', 'incorrect_answer2', 'incorrect_answer3']
    template_name = 'quiz_app/question_form.html'

    def get_initial(self):
        """
        Initialize the form with the specific quiz instance.
        """
        initial = super().get_initial()
        initial['quiz'] = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        return initial

    def get_context_data(self, **kwargs):
        """
        Add the quiz and question count to the context for rendering the form.
        """
        context = super().get_context_data(**kwargs)
        quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        context['quiz'] = quiz
        context['question_count'] = quiz.question_set.count()
        return context

    def form_valid(self, form):
        """
        Assign the quiz instance to the question and handle any errors during form submission.
        """
        try:
            form.instance.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
            response = super().form_valid(form)
            print("Form is valid and saved successfully.")
            return response
        except Exception as e:
            print(f"Error in form_valid: {e}")
            raise

    def get_success_url(self):
        """
        Redirect to the question creation page for the same quiz upon successful form submission.
        """
        return reverse_lazy('question-creator', kwargs={'pk': self.kwargs['pk']})
    

def leaderboard(request):
    """
    Render a leaderboard page showing the top 10 users based on their total scores.
    """
    leaderboard_data = (
        UserQuizProgress.objects
        .values('user__username', 'user__profile__image')
        .annotate(total_score=Sum('score'))
        .order_by('-total_score')[:10]  # Top 10 users
    )

    context = {
        'leaderboard': leaderboard_data
    }
    return render(request, 'quiz_app/leaderboard.html', context)