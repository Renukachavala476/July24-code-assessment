from django.db import models

# Create your mo(dels here.
class AdminModel(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class AddSellerModel(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    shopname=models.CharField(max_length=50)
    mobile=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

