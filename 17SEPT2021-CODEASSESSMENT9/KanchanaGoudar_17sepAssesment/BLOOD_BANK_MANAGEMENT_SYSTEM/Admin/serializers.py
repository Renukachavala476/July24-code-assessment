from rest_framework import serializers
from Admin.models import Admin,Donor

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('id','Adminname','Username','Password')

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('id','Name','Address','Bgroup','Mobilenumber','Username','Password')
