from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bankbalance=models.IntegerField()
    mobnum=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.IntegerField()

class Admin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    adminname=models.CharField(max_length=50,default=True)
