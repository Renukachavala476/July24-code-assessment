from manufacturer.models import Manu,Customer
from rest_framework import fields, serializers

class ManuSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','name','username','password')


class CustomerSerializer(serializers.ModelSerializer):
    customer_photo =serializers.ImageField()
    customer_idfile=serializers.ImageField()
    class Meta:
        model = Customer
        fields = ("customer_name", "customer_DOB", "gender", "address", "pincode", "mobileno", "email", "adharno", "product_type", "customer_username","customer_password", "customer_photo", "customer_idfile","created", "id")
