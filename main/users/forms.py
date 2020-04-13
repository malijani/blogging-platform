from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = (
            'first_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = "نام : "
        self.fields['username'].label = 'نام کاربری : '
        self.fields['email'].label = 'رایانامه : '
        self.fields['password1'].label = 'رمز عبور : '
        self.fields['password2'].label = 'تایید رمز عبور : '

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
        ]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = "نام : "
        self.fields['username'].label = 'نام کاربری : '
        self.fields['email'].label = 'رایانامه : '


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['image'].label = 'تصویر نمایه : '