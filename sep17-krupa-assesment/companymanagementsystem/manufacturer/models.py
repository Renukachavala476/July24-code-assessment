from django.db import models

# Create your models here.

class Sign(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=100)

class seller(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    shopname=models.CharField(max_length=100)
    mno=models.CharField(max_length=100)

    