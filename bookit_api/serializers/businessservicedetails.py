from rest_framework import serializers

from bookit_api.models.businessservicedetails import BusinessServiceDetails
from bookit_api.serializers.businessserializer import BusinessSerializer
from bookit_api.serializers.serviceserializer import ServiceSerializer


class BusinessServiceDetailsSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = BusinessServiceDetails
        fields = '__all__'
        read_only_fields = ['businessservice_id']