from django.db import models

# Create your models here.


    
# class customer(models.Model):
#     name=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)
#     bankbalance=models.BigIntegerField()
#     mobile=models.BigIntegerField()
#     username=models.CharField(max_length=50)
#     password=models.BigIntegerField()

class AddloginModel(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

