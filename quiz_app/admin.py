from django.contrib import admin
from .models import Quiz, Question, UserQuizProgress

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserQuizProgress)
