from django.shortcuts import render,redirect
from books.forms import BookForm

from books.models import Book

# Create your views here.

def home(request):
    return render(request,'home.html')
def add_books(request):
    if request.method=="POST":
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        #     data=form_instance.cleaned_data
        # t=data['title']
        # a=data['author']
        # p=data['pages']
        # pr=data['price']
        # l=data['language']
        # print(data)
        # b=Book.objects.create(title=t,author=a,price=pr,pages=p,language=l)
        # b.save()
        return redirect('books:viewbooks')
    if request.method=="GET":
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request,'add.html',context)
def view_books(request):
    b=Book.objects.all()
    context={'books':b}
    return render(request,'viewbooks.html',context)

def bookdetails(request,i):
    if request.method=='GET':
        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request,'bookdetails.html',context)

def editbook(request,i):
    if request.method=="POST":
        b=Book.objects.get(id=i)
        form_instance=BookForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')
    if request.method=='GET':
        b = Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context = {'form': form_instance}
        return render(request,'editbook.html',context)

def deletebook(request,i):
    if request.method=='GET':
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')