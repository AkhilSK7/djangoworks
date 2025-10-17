from django.shortcuts import render

# Create your views here.

def users(request):
    if request.method=='GET':
        return render(request,'first.html')
    if request.method=='POST':
        password=request.POST['password']
        user=request.POST['user']
        if password=='123' and user=='akhil@gmail.com':
            context={'result':2}
        return render(request,'first.html',context)