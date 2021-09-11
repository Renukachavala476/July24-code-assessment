from rest_framework import serializers
from bloodbank.models import Donor
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('id','name','address','mobilenumber','bloodgroup','username','password','donorcode')