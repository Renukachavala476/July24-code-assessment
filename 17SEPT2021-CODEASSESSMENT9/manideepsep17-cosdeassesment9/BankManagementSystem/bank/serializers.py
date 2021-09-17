from rest_framework import serializers
from bank.models import bank,AdminRegisterModel,AdminloginModel

class bankSerializer(serializers.ModelSerializer):
    class Meta:
        model=bank
        fields=('id','name','address','bankbalance','mobile','username','password')

class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminRegisterModel
        fields=('id','ename','eemail','epassword','emobile')

class AdminloginSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminloginModel
        fields=('id','eusername','epassword')