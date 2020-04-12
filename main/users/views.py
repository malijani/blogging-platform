from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register(request):
    # if data is submited
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # if form is valid when it is submited
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'حساب کاربری شما ساخته شد. الآن میتونید وارد حساب خودتون بشید!')
            return redirect('users:login')
    else:
        # create a user creation form
        form = UserRegisterForm()
    template_name = 'users/register.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def profile(request):
    template_name = 'users/profile.html'
    context = {

    }
    return render(request, template_name, context)