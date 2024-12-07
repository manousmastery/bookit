from rest_framework import serializers

from bookit_api.models import BusinessUser
from bookit_api.serializers.businessserializer import BusinessSerializer
from bookit_api.serializers.userserializer import UserSerializer


class BusinessMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    business = BusinessSerializer(read_only=True)

    class Meta:
        model = BusinessUser
        fields = ['businessuser_id', 'user', 'business', 'role', 'joined_at']
        read_only_fields = ['businessuser_id']