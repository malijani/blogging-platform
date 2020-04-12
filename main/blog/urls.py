from django.urls import path

from . import apps, views

app_name = apps.BlogConfig.name

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('about/', views.about, name='about'),
]
