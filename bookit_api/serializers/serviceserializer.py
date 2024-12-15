from rest_framework import serializers
from bookit_api.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_id', 'name', 'description']
        read_only_fields = ['service_id']