from django.db import models

class Manufacturer(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

from django.db import models

class Seller(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default='admin')
