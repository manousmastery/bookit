from rest_framework import serializers
from ..models import Business, BusinessStaffMember

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class BusinessStaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessStaffMember
        fields = '__all__'