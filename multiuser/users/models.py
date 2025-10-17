from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)