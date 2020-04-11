from django.urls import path

from . import apps, views

app_name = apps.BlogConfig.name

urlpatterns = [
    path('', views.home, name='blog-home'),
]
