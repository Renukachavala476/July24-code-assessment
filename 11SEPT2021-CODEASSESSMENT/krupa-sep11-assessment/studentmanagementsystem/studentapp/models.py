from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=40,default='',blank=True)
    address=models.CharField(max_length=40,default='',blank=True)
    clas=models.CharField(max_length=40,default='',blank=True)
    mno=models.CharField(max_length=40,default='',blank=True)
    username=models.CharField(max_length=40,default='',blank=True)
    password = models.CharField(max_length=40, default='', blank=True)