from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    """
    Handle user registration.

    If the request method is POST, this view processes the registration form submission.
    On successful registration, it saves the new user and redirects to the login page with a success message.
    If the request method is GET, it displays an empty registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration template or a redirect to the login page.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank you for creating an account, {username}. You can now log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """
    View to handle the display and submission of the profile update form.
    Allows users to update their username and email.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile_update.html', context)

def login(request):
    """
    Handle user login.

    If the request method is POST, this view processes the login form submission.
    On successful authentication, it logs the user in and redirects to the profile page with a success message.
    If the request method is GET, it displays an empty login form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login template or a redirect to the profile page.
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