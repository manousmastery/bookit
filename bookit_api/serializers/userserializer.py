from rest_framework import serializers
from bookit_api.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'phone_number', 'is_admin']
        read_only_fields = ['user_id']