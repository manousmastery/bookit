from bookit_api.models import Business
from bookit_api.serializers.userserializer import UserSerializer
from rest_framework import serializers


class BusinessSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Business
        fields = ['business_id', 'name', 'owner', 'description', 'latitude', 'longitude', 'address']
        read_only_fields = ['business_id']
