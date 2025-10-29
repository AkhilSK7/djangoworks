"""
URL configuration for schoolapp project.

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

from django.urls import path
app_name='app1'
from app1 import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('register',views.Register.as_view(),name='register'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('adminhome',views.Adminhome.as_view(),name='adminhome'),
    path('userhome',views.Userhome.as_view(),name='userhome'),
    path('schoollist',views.Schoollist.as_view(),name='schoollist'),
    path('addschool',views.Addschool.as_view(),name='addschool'),
    path('schooldetails/<int:i>',views.Schooldetails.as_view(),name='schooldetails'),
    path('studentjoin/<int:i>',views.Studentjoinview.as_view(),name='studentjoin'),
    path('leaveschool/<int:i>/<int:j>',views.Leaveschool.as_view(),name='leaveschool'),
]
