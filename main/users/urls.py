from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


from . import apps
from . import views as user_views

app_name = apps.UsersConfig.name

urlpatterns = [
    # REGISTER SECTION
    path('register/', user_views.register, name='register'),
    # UPDATE PROFILE SECTION
    path('profile/', user_views.profile, name='profile'),
    # LOG IN/OUT SECTION
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # PASSWORD RESET SECTION
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset/reset.html',
            email_template_name = 'users/password_reset/email.html',
            success_url=reverse_lazy('users:password_reset_done'),
            ),
        name='password_reset'
        ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset/done.html',
            ),
        name='password_reset_done'
        ),

    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset/confirm.html',
            success_url=reverse_lazy('users:password_reset_complete'),
            ),
        name='password_reset_confirm'
        ),

    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset/complete.html',
        ),
        name='password_reset_complete'

    ),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
