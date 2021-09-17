from rest_framework import serializers
from bank.models import Bank,Customer 


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields=("id","bankname","username","password")

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("id","name","address","bankbal","mobileno","username","password")