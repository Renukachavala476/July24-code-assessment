from django.db import models

# Create your models here.
class Admin(models.Model):
    Adminname=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

class Donor(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Bgroup=models.CharField(max_length=50)
    Mobilenumber=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)