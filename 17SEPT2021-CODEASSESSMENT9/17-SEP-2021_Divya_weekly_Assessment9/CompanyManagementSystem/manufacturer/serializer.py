from django.db.models import fields
from rest_framework import serializers
from manufacturer.models import Manufacturer,Seller

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields = ("id","name","address","email","mobile_no","username","password")

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields = ("id","sellname","selladdress","shop_name","sellmobile","sellusername","sellpassword")