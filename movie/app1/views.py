from django.shortcuts import render, redirect
from app1.forms import Movieform
from app1.models import Moviedetails

# Create your views here.
def movielist(request):
    m=Moviedetails.objects.all()
    context={'movies':m}
    return render(request,'movielist.html',context)

def addmovie(request):
    if (request.method=='POST'):
        form_instance=Movieform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:movielist')

    if (request.method=='GET'):
        form_instance=Movieform()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)

def moviedetails(request,i):
    if request.method=='GET':
        m=Moviedetails.objects.get(id=i)
        context={'movie':m}
        return render(request,'moviedetails.html',context)
def updatemovie(request,i):
    if request.method=='POST':
        m=Moviedetails.objects.get(id=i)
        form_instance=Movieform(request.POST,request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:movielist')
    if request.method=='GET':
        m=Moviedetails.objects.get(id=i)
        form_instance=Movieform(instance=m)
        context={'form':form_instance}
        return render(request,'updatemovie.html',context)

def deletemovie(request,i):
    if request.method=='GET':
        m=Moviedetails.objects.get(id=i)
        m.delete()
        return redirect('app1:movielist')