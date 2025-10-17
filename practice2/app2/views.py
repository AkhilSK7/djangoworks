from django.shortcuts import render

# Create your views here.

def movielist(request):
    return render(request,'second.html')

def movie(request):
    return render(request,'third.html')
