from django.db import models

# Create your models here.

class Moviedetails(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    language=models.CharField(max_length=100)
    year=models.IntegerField()
    director=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
