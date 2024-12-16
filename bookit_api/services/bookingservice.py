from django.core.exceptions import ValidationError
from django.db import transaction
from bookit_api.models import Booking, User, Business
from bookit_api.serializers.bookingserializer import BookingSerializer


class BookingService:
    def create_booking(self, client_id, employee_id, business_id, booking_date):
        """
        Create a new booking with the given details.
        """
        try:
            with transaction.atomic():
                client = User.objects.get(user_id=client_id)
                employee = User.objects.get(user_id=employee_id)
                business = Business.objects.get(business_id=business_id)

                booking = Booking.objects.create(
                    client=client,
                    employee=employee,
                    business=business,
                    booking_date=booking_date,
                    status='PENDING'
                )
                return BookingSerializer(booking).data
        except User.DoesNotExist:
            raise ValidationError("Client or employee not found.")
        except Business.DoesNotExist:
            raise ValidationError("Business not found.")
        except Exception as e:
            raise ValidationError(f"Failed to create booking: {str(e)}")

    def cancel_booking(self, booking_id):
        """
        Cancel a booking by updating its status.
        """
        try:
            booking = Booking.objects.get(booking_id=booking_id)
            if booking.status == 'COMPLETED':
                raise ValidationError("Cannot cancel a completed booking.")

            booking.status = 'CANCELLED'
            booking.save()
            return {"success": f"Booking with ID {booking_id} has been cancelled."}
        except Booking.DoesNotExist:
            raise ValidationError(f"Booking with ID {booking_id} not found.")
        except Exception as e:
            raise ValidationError(f"Failed to cancel booking: {str(e)}")

    def update_booking(self, booking_id, updated_data):
        """
        Update booking details such as status or booking date.
        """
        try:
            booking = Booking.objects.get(booking_id=booking_id)
            serializer = BookingSerializer(booking, data=updated_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data
        except Booking.DoesNotExist:
            raise ValidationError(f"Booking with ID {booking_id} not found.")
        except Exception as e:
            raise ValidationError(f"Failed to update booking: {str(e)}")

    def get_booking(self, booking_id):
        """
        Retrieve details of a specific booking by ID.
        """
        try:
            booking = Booking.objects.get(booking_id=booking_id)
            return BookingSerializer(booking).data
        except Booking.DoesNotExist:
            raise ValidationError(f"Booking with ID {booking_id} not found.")
        except Exception as e:
            raise ValidationError(f"Failed to retrieve booking: {str(e)}")

    def get_bookings_by_business(self, business_id):
        """
        Retrieve all bookings for a specific business.
        """
        try:
            bookings = Booking.objects.filter(business_id=business_id)
            return BookingSerializer(bookings, many=True).data
        except Exception as e:
            raise ValidationError(f"Failed to retrieve bookings: {str(e)}")
