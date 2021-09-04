from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_code=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50)
    username=models.CharField(max_length=50,default='No Name',blank='True')
    password=models.CharField(max_length=50,default='No Name',blank='True')
    