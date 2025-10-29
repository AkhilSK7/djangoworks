from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from app1.models import School,Student

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']

class Loginform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())

class Addschoolform(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'

class Studentjoinform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','place']
