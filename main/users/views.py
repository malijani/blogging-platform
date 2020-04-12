from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    # make updates if form submited
    if request.method == "POST":

        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
         )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'حساب کاربری شما بروز رسانی شد!')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # configure frontend
    template_name = 'users/profile.html'
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, template_name, context)