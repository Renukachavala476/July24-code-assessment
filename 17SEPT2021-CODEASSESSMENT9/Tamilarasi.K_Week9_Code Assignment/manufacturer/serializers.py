from rest_framework import serializers
from manufacturer.models import Admin,Seller

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=("id","adminname","username","password")

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('id','name','address','shopname','mobilenumber','username','password')
        