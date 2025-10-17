"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views
app_name='books'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    path('',views.Home.as_view(),name='home'),
    # path('addbooks',views.add_books,name='addbooks'),
    path('addbooks',views.Addbook.as_view(),name='addbooks'),
    # path('view',views.view_books,name='viewbooks'),
    path('viewbooks',views.Viewbooks.as_view(),name='viewbooks'),
    path('details/<int:i>',views.Bookdetails.as_view(),name='details'),
    path('edit/<int:i>',views.Editbook.as_view(),name='edit'),
    path('delete/<int:i>',views.Deletebook.as_view(),name='delete'),
    path('search',views.Searchbook.as_view(),name='search'),
]
