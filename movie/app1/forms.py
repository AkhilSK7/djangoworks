from django import forms
from app1.models import Moviedetails

class Movieform(forms.ModelForm):
    class Meta:
        model=Moviedetails
        fields='__all__'