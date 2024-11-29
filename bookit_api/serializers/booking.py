from rest_framework import serializers
from ..models.booking import Booking

class Bookingerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
