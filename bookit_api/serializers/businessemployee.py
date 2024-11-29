from rest_framework import serializers
from ..models.businessemployee import BusinessEmployee

class BusinessEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessEmployee
        fields = '__all__'
