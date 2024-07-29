from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """
    A form for registering new users.

    This form extends the built-in UserCreationForm to include an email field.
    It is used to collect the necessary information for user registration.
    """
    email = forms.EmailField()

    class Meta: 
        """
        Meta class for configuring the form's model and fields.

        - `model`: Specifies the User model to be used.
        - `fields`: Defines the fields to be included in the form.
        """
        model = User 
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating existing user information.

    This form is used to update the user's username and email address.
    """
    email = forms.EmailField()

    class Meta: 
        """
        Meta class for configuring the form's model and fields.

        - `model`: Specifies the User model to be used.
        - `fields`: Defines the fields to be included in the form.
        """
        model = User 
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating user profile information.

    This form is used to update the user's profile image.
    """
    class Meta: 
        """
        Meta class for configuring the form's model and fields.

        - `model`: Specifies the Profile model to be used.
        - `fields`: Defines the fields to be included in the form.
        """
        model = Profile
        fields = ['image']