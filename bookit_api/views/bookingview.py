from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers.bookingserializer import BookingSerializer
from ..services.bookingservice import BookingService

booking_service =  BookingService()

@swagger_auto_schema(
    method='post',
    operation_description="create a booking",
    responses={200: BookingSerializer(many=False)},
)
@api_view(['POST'])
def create_booking(request) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    booking_data = request.data
    try:
        booking_date = datetime.strptime(booking_data['booking_date'], '%Y-%m-%d')
        employee_id = int(booking_data['employee_id'])
        business_id = int(booking_data['business_id'])
    except ValueError as e:
        return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    result = booking_service.create_booking(
        employee_id=employee_id,
        booking_date=booking_date,
        client_id=user.user_id,
        business_id=business_id
    )
    return Response(result)