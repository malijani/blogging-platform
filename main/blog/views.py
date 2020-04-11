from django.shortcuts import render


def home(request):
    # Frontend configuration
    template_name = 'blog/home.html'
    context = {

    }
    return render(request, template_name, context)


def about(request):
    # Frontend configuration
    template_name = 'blog/about.html'
    context = {

    }
    return render(request, template_name, context)
