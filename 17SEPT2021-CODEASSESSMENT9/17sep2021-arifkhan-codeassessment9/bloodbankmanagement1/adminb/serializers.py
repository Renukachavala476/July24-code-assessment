from rest_framework import serializers
from adminb.models import BloodAd,Donor

class BloodAdSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodAd
        fields=("id","username","password")


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('id','name','address','bloodg','mobile','username','password')