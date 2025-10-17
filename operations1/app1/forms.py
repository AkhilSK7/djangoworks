from django import forms

class AdditionForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class BmiForm(forms.Form):
    weight=forms.IntegerField()
    height=forms.FloatField()

class SignupForm(forms.Form):
    gender_choices=(("male","Male"),("female","Female"))#male->send to backend Male->to display
    role_choices=(("admin","Admin"),("user","User"))
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    place=forms.CharField()
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role=forms.ChoiceField(choices=role_choices)
    email=forms.EmailField()

class CalorieForm(forms.Form):
    gender_choices = (("male", "Male"), ("female", "Female"))
    activity_choices=(("1.2","sedentary"),("1.375","lightly active"),("1.55","moderatly active"),("1.725","Very active"),("1.9","Extra active"))
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    Weight=forms.IntegerField()
    Height=forms.IntegerField()
    Age=forms.IntegerField()
    Activity_level=forms.ChoiceField(choices=activity_choices)
