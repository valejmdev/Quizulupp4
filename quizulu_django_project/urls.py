from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    # User registration page
    path('register/', user_views.register, name='register'),
    # User profile page
    path('profile/', user_views.profile, name='profile'),
    # Login page
    path('login/', auth_views.LoginView.as_view(
         template_name='users/login.html'), name='login'),
    # Logout page
    path('logout/', auth_views.LogoutView.as_view(
         template_name='users/logout.html'), name='logout'),
    # Password reset page
    path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name='users/password_reset.html'), name='password_reset'),
    # Password reset done page (confirmation)
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
         template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    # Password reset confirmation page
    path('password-reset-confrim/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
          template_name='users/password_reset_confirm.html'),
         name='password_reset'),
    # Password reset complete page
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
          template_name='users/password_reset_complete.html'),
         name='password_reset'),
    # Include URLs from the quiz_app application
    path('', include('quiz_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)