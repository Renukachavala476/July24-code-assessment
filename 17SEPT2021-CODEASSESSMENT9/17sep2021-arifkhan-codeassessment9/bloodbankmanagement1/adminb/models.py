from django.db import models
class BloodAd(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class Donor(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bloodg=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default='admin')
