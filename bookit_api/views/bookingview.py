from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers.bookingserializer import BookingSerializer
from ..services.bookingservice import BookingService

booking_service = BookingService()


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
        businessservice_id = int(booking_data['businessservice_id'])
    except ValueError as e:
        return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    result = booking_service.create_booking(
        employee_id=employee_id,
        booking_date=booking_date,
        client_id=user.user_id,
        businessservice_id=businessservice_id,
    )
    return Response(result)


@swagger_auto_schema(
    method='put',
    operation_description="cancel a booking",
    responses={200: BookingSerializer(many=False)},
)
@api_view(['PUT'])
def cancel_booking(request, booking_id: int) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    result = booking_service.cancel_booking(booking_id)
    return Response(result)


@swagger_auto_schema(
    method='put',
    operation_description="update a booking",
    responses={200: BookingSerializer(many=False)},
)
@api_view(['PUT'])
def update_booking(request, booking_id: int) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    booking_data = request.data
    result = booking_service.update_booking(booking_id, booking_data)
    return Response(result)


@swagger_auto_schema(
    method='get',
    operation_description="get a booking",
    responses={200: BookingSerializer(many=False)},
)
@api_view(['GET'])
def get_booking(request, booking_id: int) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    result = booking_service.get_booking(booking_id)
    return Response(result)


@swagger_auto_schema(
    method='get',
    operation_description="get bookings by business",
    responses={200: BookingSerializer(many=True)},
)
@api_view(['GET'])
def get_booking_by_business(request, business_id: int) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    result = booking_service.get_bookings_by_business(business_id)
    return Response(result)


@swagger_auto_schema(
    method='get',
    operation_description="get bookings by client",
    responses={200: BookingSerializer(many=True)},
)
@api_view(['GET'])
def get_booking_by_client(request) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    result = booking_service.get_bookings_by_client(user.user_id)
    return Response(result)


@swagger_auto_schema(
    method='get',
    operation_description="get bookings by employee",
    responses={200: BookingSerializer(many=True)},
)
@api_view(['GET'])
def get_booking_by_employee(request) -> Response:
    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    result = booking_service.get_bookings_by_employee(user.user_id)
    return Response(result)
