from django.urls import path

from . import apps, views

app_name = apps.BlogConfig.name

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('user/<str:username>/', views.UserPostsListView.as_view(), name='profile'),
    path('post/create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('about/', views.about, name='about'),
]
