from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from users.forms import SignupForm,Loginform


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')
class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')
class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)

class Userlogin(View):
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)

            if user and user.is_superuser==True:
                login(request,user)
                return redirect('users:adminhome')
            elif user and user.role=='student':
                login(request,user)
                return redirect('users:studenthome')
            elif user and user.role=='teacher':
                login(request,user)
                return redirect('users:teacherhome')
            else:
                messages.error(request,"Invalid user credentials")
                return render(request,'login.html',{'form':form_instance})


class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')

