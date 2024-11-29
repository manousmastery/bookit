from rest_framework import serializers
from ..models.businessservice import BusinessService

class BusinessEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessService
        fields = '__all__'
