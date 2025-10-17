from django.http import HttpResponse
from django.shortcuts import render

# # Create your views here.
# def first.html(request):
#     return HttpResponse("First page")
#
# def second(request):
#     return HttpResponse("Second page")

def first(request):
    d={'name':'Arun','age':22}
    return render(request,'firstpage.html',context=d)

def second(request):
    context={'name':'facebook','button':'login'}
    return render(request,'secondpage.html',context)