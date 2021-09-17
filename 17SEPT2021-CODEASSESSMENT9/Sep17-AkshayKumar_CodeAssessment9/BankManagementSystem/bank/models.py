from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    bankbalance= models.IntegerField()
    mobno = models.BigIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Admin(models.Model):
    aname = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)