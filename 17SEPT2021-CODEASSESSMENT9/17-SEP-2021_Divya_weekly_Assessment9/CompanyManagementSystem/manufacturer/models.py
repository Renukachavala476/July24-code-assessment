import manufacturer
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Manufacturer(models.Model):
    name = CharField(max_length=50)
    address = CharField(max_length=50)
    email = CharField(max_length=50)
    mobile_no = CharField(max_length=50)
    username = CharField(max_length=50)
    password = CharField(max_length=50)

class Seller(models.Model):
    sellname = CharField(max_length=50)
    selladdress = CharField(max_length=50)
    shop_name = CharField(max_length=50)
    sellmobile = CharField(max_length=50)
    sellusername = CharField(max_length=50)
    sellpassword = CharField(max_length=50)