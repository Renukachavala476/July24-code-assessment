from rest_framework import serializers
from bank.models import bank,AdminRegisterModel,AdminloginModel

class bankSerializer(serializers.ModelSerializer):
    class Meta:
        model=bank
        fields=('id','name','address','bankbalance','mobile','username','password')

class AdminRegs(serializers.ModelSerializer):
    class Meta:
        model=AdminRegisterModel
        fields=('id','ename','eemail','epassword','emobile')

class Adminlogs(serializers.ModelSerializer):
    class Meta:
        model=AdminloginModel
        fields=('id','eusername','epassword')