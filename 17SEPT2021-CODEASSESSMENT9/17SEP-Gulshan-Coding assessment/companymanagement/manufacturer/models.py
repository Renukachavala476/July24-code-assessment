from django.db import models

# Create your models here.
class Manu(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Customer(models.Model):
    customer_name=models.CharField(max_length=50, default='')
    customer_DOB=models.CharField(max_length=50,default='')
    gender=models.CharField(max_length=50, default='')
    address=models.CharField(max_length=50, default='')
    pincode=models.BigIntegerField(default='')
    mobileno=models.BigIntegerField(default='')
    email=models.EmailField(max_length=50, default='')
    adharno=models.BigIntegerField(default='')
    product_type=models.CharField(max_length=50, default='')
    customer_username=models.CharField(max_length=50, default='')
    customer_password=models.CharField(max_length=50, default='')
    customer_photo = models.ImageField(upload_to='images/', default=None)
    customer_idfile = models.ImageField(upload_to='files/', default=None)
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)
