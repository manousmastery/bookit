from rest_framework import serializers
from bookit_api.models.usermodel import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'email', 'first_name', 'last_name', 'phone_number')