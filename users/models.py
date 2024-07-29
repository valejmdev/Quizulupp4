from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    A model representing a user profile.

    This model is linked to the built-in User model via a one-to-one relationship.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the Profile instance.

        Returns:
        str: A string representing the profile with the user's username.
        """
        return f'{self.user.username} Profile'