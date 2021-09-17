from rest_framework import serializers
from manufacturer.models import Manufacturer,Seller
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields=('id','username','password')


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('id','name','address','shop_name','phone_no','username','password')