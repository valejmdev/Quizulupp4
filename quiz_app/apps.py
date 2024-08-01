from django.apps import AppConfig


class QuizAppConfig(AppConfig):
    """
    Configuration class for the Quiz application.

    This class is used to configure the 'quiz_app' Django application.
    It sets the default auto field type for models to 'BigAutoField',
    which is suitable for large datasets and provides a larger integer
    field for primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz_app'
