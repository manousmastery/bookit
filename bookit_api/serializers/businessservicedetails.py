from rest_framework import serializers

from bookit_api.models.businessservicedetails import BusinessServiceDetails


class BusinessServiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessServiceDetails
        fields = '__all__'
        read_only_fields = ['businessservice_id']