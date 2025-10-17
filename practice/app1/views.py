from django.shortcuts import render

# Create your views here.

def hello(request):
    if request.method=='POST':
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        m=n1*n2
        context={'result':m}
        return render(request,'first.html.html',context)

    if request.method=='GET':
        return render(request,'first.html.html')


