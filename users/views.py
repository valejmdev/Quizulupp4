from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    """
    Handle user registration.

    If the request method is POST,
    this view processes the registration form submission.
    On successful registration, it saves the new user and
    redirects to the login page with a success message.
    If the request method is GET, it displays an empty registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration template or
        a redirect to the login page.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Thank you for creating an account,{username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    View to handle both viewing and updating the user profile.
    Allows users to view their profile details and
    update their username and email.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if 'update' in request.POST and u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

        if 'delete' in request.POST:
            request.user.delete()
            messages.success(request, 'Your profile has been deleted.')
            return redirect('quiz-index')

    else:
        u_form = UserUpdateForm(instance=request.user)

    is_edit_mode = request.GET.get('edit') == 'true'

    context = {
        'user': request.user,
        'u_form': u_form,
        'is_edit_mode': is_edit_mode
    }

    return render(request, 'users/profile.html', context)


def login(request):
    """
    Handle user login.

    If the request method is POST,
    this view processes the login form submission.
    On successful authentication, it logs the user in and
    redirects to the profile page with a success message.
    If the request method is GET, it displays an empty login form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered login template or
        a redirect to the profile page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})
    