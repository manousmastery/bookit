from rest_framework import serializers
from bookit_api.models.servicecategory import ServiceCategory


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['servicecategory_id', 'name']
        read_only_fields = ['servicecategory_id']