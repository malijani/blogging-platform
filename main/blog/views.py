from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    #queryset = Post.objects.order_by('-date_posted')[:5]
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = 'blog/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    #context_object_name = 'post'

def about(request):
    # Frontend configuration
    template_name = 'blog/about.html'
    context = {

    }
    return render(request, template_name, context)
