from django.db import models
from django.db.models import fields
from rest_framework import serializers
from bank.models import Bankapp, Customer

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bankapp
        fields = ('id','name','address','bank_balance','mobile_no','username','password')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("id","username","password")        
   