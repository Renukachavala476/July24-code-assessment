from rest_framework import serializers
from manufacturer.models import Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields=("id","username","password")

from rest_framework import serializers
from manufacturer.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('id','name','address','sname','mobile','username','password')



