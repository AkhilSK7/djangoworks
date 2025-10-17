from django.shortcuts import render

# Create your views here.
from math import factorial as f1
def addition(request):
    if (request.method=='POST'):
        n1=int(request.POST["n1"])
        n2=int(request.POST["n2"])
        s=n1+n2
        context={'result':s}
        return render(request,'addition.html',context)
    if (request.method=='GET'):
        return render(request,'addition.html')

def factorial(request):
    if (request.method=='POST'):
        num=int(request.POST['num'])
        f=f1(num)
        context={'result':f}
        return render(request,'factorial.html',context)
    if (request.method=='GET'):
        return render(request,'factorial.html')

def bmi(request):
    if (request.method == 'POST'):
        w = float(request.POST["weight"])
        h = float(request.POST["height"])
        b = w/(h*h)
        context = {'result': b}
        return render(request, 'bmi.html', context)
    if (request.method == 'GET'):
        return render(request, 'bmi.html')