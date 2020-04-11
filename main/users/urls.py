from django.urls import path
from . import apps
from . import views

app_name = apps.UsersConfig.name

urlpatterns = [
    path('register/', views.register, name='register'),
]