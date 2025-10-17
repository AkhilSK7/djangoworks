
from django.urls import path
from users import views
app_name='users'

urlpatterns = [

    path('',views.Home.as_view(),name='home'),
    path('adminhome',views.Adminhome.as_view(),name='adminhome'),
    path('teacherhome',views.Teacherhome.as_view(),name='teacherhome'),
    path('studenthome',views.Studenthome.as_view(),name='studenthome'),
    path('register', views.Register.as_view(), name='register'),
    path('login', views.Userlogin.as_view(), name='login'),
    path('logout',views.Userlogout.as_view(),name='logout'),
    path('otpverification',views.Otpverification.as_view(),name='otp')

]
