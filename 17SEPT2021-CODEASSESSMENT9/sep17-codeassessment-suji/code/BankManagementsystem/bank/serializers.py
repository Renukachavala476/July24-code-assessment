from django.db import models
from django.db.models import fields
from rest_framework import serializers
from bank.models import Bank

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields=('id','username','password')
        