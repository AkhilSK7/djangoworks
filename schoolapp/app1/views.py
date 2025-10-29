from django.db.transaction import commit
from django.shortcuts import render,redirect
from django.views import View
from app1.forms import Signupform,Loginform,Addschoolform,Studentjoinform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app1.models import School,Student
# Create your views here.

class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class Userhome(View):
    def get(self,request):
        return render(request,'userhome.html')

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:login')
        else:
            context={'form':form_instance}
            return render(request,'register.html',context)
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'register.html',context)
class Login(View):
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
                return redirect('app1:adminhome')
            elif user and user.is_superuser==False:
                login(request,user)
                return redirect('app1:userhome')

            else:
                messages.error(request,"Invalid user credentials")
                return render(request,'login.html',{'form':form_instance})
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('app1:login')

class Schoollist(View):
    def get(self,request):
        s=School.objects.all()
        context={'school':s}
        return render(request,'schoollist.html',context)


class Addschool(View):
    def post(self,request):
        form_instance=Addschoolform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:schoollist')
        else:
            context={'form':form_instance}
            return render(request,'addschool.html',context)
    def get(self,request):
        form_instance=Addschoolform()
        context={'form':form_instance}
        return render(request,'addschool.html',context)

class Schooldetails(View):
    def get(self,request,i):
        s=School.objects.get(id=i)
        can_join=True
        is_student=False
        try:
            u=request.user
            st=Student.objects.get(user=u)
            can_join=False
            if st.school==s:
                is_student=True
        except:
            pass
        context={'school':s,'can_join':can_join,'is_student':is_student}
        return render(request,'schooldetails.html',context)

class Studentjoinview(View):
    def get(self,request,i):
        form_instance=Studentjoinform()
        context={'form':form_instance}
        return render(request,'studentjoin.html',context)
    def post(selfself,request,i):
        form_instance=Studentjoinform(request.POST)
        if form_instance.is_valid():
            s=form_instance.save(commit=False)
            sch=School.objects.get(id=i)
            s.school=sch
            u=request.user
            s.user=u
            s.save()
            return redirect('app1:userhome')


class Leaveschool(View):
    def get(self,request,i,j):
        s=Student.objects.get(school=i,user=j)
        s.delete()
        return redirect('app1:userhome')