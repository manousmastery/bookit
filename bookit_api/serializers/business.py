from rest_framework import serializers
from ..models.business import *

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class BusinessDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomain
        fields = '__all__'

class BusinessDomainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomainService
        fields = '__all__'

class BusinessDomainAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomainAssociation
        fields = '__all__'