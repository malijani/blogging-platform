from django.shortcuts import render
from .models import Post

# just a dummy post data to design frontend
# posts = [
#     {
#         'author': 'محمد علیجانی',
#         'title': 'اولین پست وبلاگ',
#         'content': 'محتوای اولین پست وبلاگ',
#         'date_posted': '۲۳ فروردین ۱۳۹۹',
#     },
# ]

def home(request):
    # QuerySet of Post objects
    queryset = Post.objects.order_by('-date_posted')
    # Frontend configuration
    template_name = 'blog/home.html'
    context = {
        'posts': queryset,
    }
    return render(request, template_name, context)


def about(request):
    # Frontend configuration
    template_name = 'blog/about.html'
    context = {

    }
    return render(request, template_name, context)
