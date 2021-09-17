from django.db import models

# Create your models here.
class Bank(models.Model):
    bankname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bankbal=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
