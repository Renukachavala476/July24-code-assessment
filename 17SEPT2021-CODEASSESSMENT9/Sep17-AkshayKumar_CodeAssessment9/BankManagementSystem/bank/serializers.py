from rest_framework import serializers
from bank.models import Admin, Customers

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id','name','address','bankbalance','mobno','username','password')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('aname','pwd')