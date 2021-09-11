from django.db import models

# Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=50,default='NO NAME',blank=True)
    address=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    donorcode=models.CharField(max_length=50)