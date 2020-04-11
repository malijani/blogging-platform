from django.shortcuts import render

# just a dummy post data to design frontend
posts = [
    {
        'author': 'محمد علیجانی',
        'title': 'اولین پست وبلاگ',
        'content': 'محتوای اولین پست وبلاگ',
        'date_posted': '۲۳ فروردین ۱۳۹۹',
    },{
        'author': 'یه بنده خدا',
        'title': 'دومین پست وبلاگ',
        'content': 'محتوای دومین پست وبلاگ',
        'date_posted': '۲۵ فروردین ۱۳۹۹',
    }
]

def home(request):
    # Frontend configuration
    template_name = 'blog/home.html'
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def about(request):
    # Frontend configuration
    template_name = 'blog/about.html'
    context = {

    }
    return render(request, template_name, context)
