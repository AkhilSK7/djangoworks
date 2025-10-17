from django.http import HttpResponse
from django.shortcuts import render


# function based view

#Home view
def Home(request):
    return HttpResponse("Welcome to new django app")

#index view
def Index(request):
    return HttpResponse("Index page")

