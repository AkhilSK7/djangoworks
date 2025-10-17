
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import Signupform,Loginform
from django.shortcuts import render,redirect
from django.views import View

# Create your views here.
class Register(View):
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'register.html',context)


class Userlogin(View):
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)
    def post(selfself,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('books:home')
            else:
                messages.error(request,"Invalid user credentials")
                return render(request,'login.html',{'form':form_instance})

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')


