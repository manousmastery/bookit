from django.utils import timezone
from rest_framework import serializers

from bookit_api.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['booking_id']

    def validate_booking_date(self, booking_date):
        """Ensure booking_date is greater than now."""
        now = timezone.now()
        if booking_date >= now:
            raise serializers.ValidationError(f"Booking date must be greater or equal to {now}.")
        return booking_date