from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    # if data is submited
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # if form is valid when it is submited
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'حساب کاربری {username} ایجاد شد!')
            return redirect('blog:home')
    else:
        # create a user creation form
        form = UserRegisterForm()
    template_name = 'users/register.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)
