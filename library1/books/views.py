from django.contrib.messages.context_processors import messages
from django.shortcuts import render,redirect
from books.forms import BookForm

from django.views import View

from books.models import Book

# Create your views here.

# def home(request):
#     return render(request,'home.html')

from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Addbook(View):
    def post(self,request):
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')
    def get(self,request):
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request,'add.html',context)
class Viewbooks(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request,'viewbooks.html',context)

class Bookdetails(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request,'bookdetails.html',context)

class Editbook(View):
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BookForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context = {'form': form_instance}
        return render(request,'editbook.html',context)

class Deletebook(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

from django.db.models import Q
from django.contrib import messages
class Searchbook(View):
    def get(self,request):
        query=request.GET['q']

        if query:
            b=Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(language__icontains=query))
            context={'books':b}
            return render(request,'search.html',context)

