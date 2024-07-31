from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a Profile instance when a new User is created.

    This signal receiver listens for the `post_save` signal
    from the User model.
    When a new User instance is created,
    it automatically creates a corresponding
    Profile instance.

    Args:
        sender (Model): The model class sending the signal (User).
        instance (User): The instance of the model being saved.
        created (bool): A boolean indicating whether
        a new instance was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save the Profile instance associated with a User when the User is saved.

    This signal receiver listens for the `post_save`
    signal from the User model.
    If a User instance has an associated Profile, this method ensures that the
    Profile instance is saved when the User is saved.

    Args:
        sender (Model): The model class sending the signal (User).
        instance (User): The instance of the model being saved.
        **kwargs: Additional keyword arguments.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
