from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration class for the 'users' Django application.

    This class defines settings and configurations for the 'users' app.
    It is used by Django to initialize the app and set up necessary configurations.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        Called when Django is fully initialized.

        This method is used to import signal handlers for the 'users' app.
        The 'users.signals' module is imported to ensure that the signal handlers 
        are registered and active when the app is ready.
        """

        import users.signals