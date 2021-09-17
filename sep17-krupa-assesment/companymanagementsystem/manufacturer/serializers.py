from rest_framework import serializers
from manufacturer.models import seller,Sign

class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=seller
        fields=('id','name','address','mno','shopname','username','password')


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sign
        fields=('id','username','password')