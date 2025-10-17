from django.shortcuts import render

from app1.forms import AdditionForm,BmiForm,SignupForm,CalorieForm
from math import factorial as f1
# Create your views here.

def addition(request):
    if request.method=='POST':
       print(request.POST) #submitted data
       #creating a form instance using submitted data
       form_instance=AdditionForm(request.POST)
       #check whether data is valid
       if form_instance.is_valid():
           #process data
           data=form_instance.cleaned_data #validated data
           print(data)
           n1=data['num1']
           n2=data['num2']
           s=n1+n2
           context={'result':s,'form':form_instance}#this time form_instance have data so it will be displayed
           return render(request,'addition.html',context)

    if request.method=='GET':
        form_instance=AdditionForm() #empty form object
        context={'form':form_instance}
        return render(request,'addition.html',context)

def bmi(request):
    if (request.method == 'POST'):
        print(request.POST)
        form_instance=BmiForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            w=data['weight']
            h=data['height']
            b = w / (h * h)
            context={'result':b,'form':form_instance}
            return render(request,'bmi.html',context)
    if (request.method == 'GET'):
        form_instance=BmiForm()
        context={'form':form_instance}
        return render(request, 'bmi.html',context)


def signup(request):
    if request.method=='POST':
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            context={'form':form_instance}
            return render(request,'signup.html',context)

    if request.method=='GET':
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'signup.html',context)

def calorie(request):
    if request.method=='POST':
        form_instance=CalorieForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            gender=data['gender']
            w=data['Weight']
            h=data['Height']
            age=data['Age']
            activity=float(data['Activity_level'])
            if gender=='male':
                bmr=10*w+6.25*h-5*age+5
                calorie=int(round(bmr*activity,0))
                context = {'form': form_instance, 'calorie': calorie}
            elif gender=='female':
                bmr=10*w+6.25*h-5*age-161
                calorie = int(round(bmr * activity, 0))
                context = {'form': form_instance,'calorie':calorie}
            return render(request,"calorie.html",context)

    if request.method=='GET':
        form_instance=CalorieForm()
        context={'form':form_instance}
        return render(request,'calorie.html',context)


