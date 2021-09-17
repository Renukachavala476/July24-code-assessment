from django.db import models

# Create your models here.
class Bankapp(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    bank_balance = models.IntegerField()
    mobile_no =models.BigIntegerField()
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Customer(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
