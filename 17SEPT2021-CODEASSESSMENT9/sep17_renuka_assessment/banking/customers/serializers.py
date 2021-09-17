from rest_framework import serializers
from customers.models import AddloginModel
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddloginModel
        fields=('id','username','password')