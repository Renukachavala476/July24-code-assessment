from rest_framework import serializers
from BloodAdmin.models import BloodAdmin,Donor

class BloodAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodAdmin
        fields=("id","username","password")


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('id','name','address','bloodg','mobile','username','password')



