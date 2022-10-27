from django.db import models

# Create your models here.
class Table1(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)

class Image(models.Model):
    Imagename=models.CharField(max_length=10)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)