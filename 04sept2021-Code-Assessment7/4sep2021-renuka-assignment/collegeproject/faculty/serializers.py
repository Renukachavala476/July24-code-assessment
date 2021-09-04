from rest_framework import serializers
from faculty.models import Faculty
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('id','faculty_code','name','address','department','mobilenumber','username','password')
