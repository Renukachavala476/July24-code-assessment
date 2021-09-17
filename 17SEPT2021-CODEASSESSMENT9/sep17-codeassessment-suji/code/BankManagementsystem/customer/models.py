from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bankbalance=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
