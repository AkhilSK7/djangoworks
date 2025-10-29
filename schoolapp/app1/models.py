from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=30)
    principal=models.CharField(max_length=20)
    location=models.CharField(max_length=30)

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    user=models.OneToOneField(User,on_delete=models.CASCADE)