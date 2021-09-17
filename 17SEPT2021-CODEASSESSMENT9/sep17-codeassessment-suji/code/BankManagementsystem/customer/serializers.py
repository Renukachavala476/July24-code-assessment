from django.db import models
from django.db.models import fields
from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('name','address','bankbalance','mobilenumber','username','password')