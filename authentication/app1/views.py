from django.shortcuts import render,redirect
from django.views import View
from app1.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:userlogin')
        else:
            print("Error")
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance = Signupform()
        context={'form':form_instance}
        return render(request,'register.html',context)

class Login(View):
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            #authenticate returns userobject if username and password exists
            #else returns none
            if user:#if user exists
                login(request,user)#login adds current user into session
                return redirect('app1:home')
            else:#if user doesnt exist
                messages.error(request,"Invalid user credentials")
                return render(request,'login.html',{'form':form_instance})
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('app1:userlogin')