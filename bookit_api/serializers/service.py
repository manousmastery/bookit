from rest_framework import serializers

from ..models.schedule import Schedule
from ..models.service import Service

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
