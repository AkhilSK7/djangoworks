from django.shortcuts import render, redirect
from app1.forms import Employeeform
from app1.models import Employee
# Create your views here.
def home(request):
    if request.method=='GET':
        return render(request,'home.html')

def addemployee(request):
    if request.method=='POST':
        f=Employeeform(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return redirect('app1:add')
    if request.method=='GET':
        f=Employeeform()
        context={"form":f}
        return render(request,'addemployee.html',context)

def viewemployee(request):
    if request.method=="GET":
        f=Employee.objects.all()
        context={'form':f}
        return render(request,'viewemployee.html',context)
