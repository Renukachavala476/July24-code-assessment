from rest_framework import serializers
from sellers.models import seller


class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=seller
        fields=('id','name','address','mno','shopname','username','password')

