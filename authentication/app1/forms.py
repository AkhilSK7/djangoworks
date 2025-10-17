from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)