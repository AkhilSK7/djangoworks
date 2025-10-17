from django.shortcuts import render

# Create your views here.

def second(request):
    context={'name':'arun','age':25}
    return render(request,'second.html',context)
