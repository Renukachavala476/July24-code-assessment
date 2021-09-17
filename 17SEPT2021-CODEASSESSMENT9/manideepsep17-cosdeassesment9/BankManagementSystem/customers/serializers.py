from rest_framework import serializers
from customers.models import AddloginModel




class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddloginModel
        fields=('id','username','password')

# class bankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=bank
#         fields=('id','name','address','bankbalance','mobile','username','password')
