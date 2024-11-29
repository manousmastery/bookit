from rest_framework import serializers
from ..models import BusinessUserAssociation

class BusinessUserAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUserAssociation
        fields = '__all__'