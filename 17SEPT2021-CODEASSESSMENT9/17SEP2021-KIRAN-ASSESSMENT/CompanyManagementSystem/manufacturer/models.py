from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    username=models.CharField(max_length=50,default='No Name',blank='True')
    password=models.CharField(max_length=50,default='No Name',blank='True')
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)


class Seller(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    shop_name=models.CharField(max_length=50)
    phone_no=models.BigIntegerField()
    username=models.CharField(max_length=50,default='No Name',blank='True')
    password=models.CharField(max_length=50,default='No Name',blank='True')