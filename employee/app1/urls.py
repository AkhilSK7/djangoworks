
from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.addemployee,name="add"),
    path('details/',views.viewemployee,name="details")
]
