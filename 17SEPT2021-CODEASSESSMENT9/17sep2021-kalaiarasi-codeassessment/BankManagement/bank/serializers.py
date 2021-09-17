from rest_framework import serializers
from bank.models import Customer, Admin

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','name','address','bankbalance','mobnum','username','password')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('id','username','password','adminname')

