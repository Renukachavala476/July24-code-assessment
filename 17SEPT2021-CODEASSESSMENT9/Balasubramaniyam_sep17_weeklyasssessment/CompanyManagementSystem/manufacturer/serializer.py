from django.db import models
from django.db.models import fields
from manufacturer.models import AdminModel,AddSellerModel
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminModel
        fields=("id","name","username","password")

class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddSellerModel
        fields=("id","name","address","shopname","mobile","username","password")
