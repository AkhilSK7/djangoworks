from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()
    image=models.ImageField(upload_to="employees")



