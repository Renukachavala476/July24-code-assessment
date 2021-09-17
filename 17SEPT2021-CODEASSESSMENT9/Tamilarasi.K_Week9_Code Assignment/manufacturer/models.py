from django.db import models

# Create your models here.

class Admin(models.Model):
    adminname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Seller(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    shopname=models.CharField(max_length=20)
    mobilenumber=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)