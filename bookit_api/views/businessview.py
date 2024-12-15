from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..helpers import BusinessServiceDetailsParams
from ..serializers.businessserializer import BusinessSerializer
from ..serializers.businessservicedetails import BusinessServiceDetailsSerializer
from ..services.businessservice import BusinessService

business_service =  BusinessService()

@swagger_auto_schema(
    method='get',
    operation_description="Get all business",
    responses={200: BusinessSerializer(many=True)},
)
@api_view(['GET'])
def get_all_business(request) -> Response:
    return Response(business_service.get_all())

@swagger_auto_schema(
    method='get',
    operation_description="Get business info",
    responses={200: BusinessSerializer(many=False)},
)
@api_view(['GET'])
def get_business_info(request, business_id: int) -> Response:
    business_info = business_service.get_business_info(business_id)
    return Response(data=business_info)

@swagger_auto_schema(
    method="post",
    operation_description="Service add endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "service_id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="service_id"
            ),
            "price": openapi.Schema(
                type=openapi.TYPE_NUMBER, description="service price"
            ),
            "duration": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="service duration"
            ),
            "showed_name": openapi.Schema(
                type=openapi.TYPE_STRING, description="service name"
            ),
            "showed_description": openapi.Schema(
                type=openapi.TYPE_STRING, description="Service description"
            ),

        },
        required=["service_id", "price", "duration"],
    ),
    responses={
        200: BusinessServiceDetailsSerializer,
        400: openapi.Response(description="Invalid data provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(['POST'])
def add_service_for_business(request, business_id):
    try:
        service_details_params = BusinessServiceDetailsParams(
            business_id=business_id,
            service_id=request.data['service_id'],
            price=request.data['price'],
            duration=request.data['duration'],
            showed_name=request.data['showed_name'],
            showed_description=request.data['showed_description'],
        )
        service_details_params.validate_details_to_add()
        result = business_service.add_service_for_business(service_details_params)
        return Response(data=result, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method="put",
    operation_description="Service update endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "service_id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="service_id"
            ),
            "price": openapi.Schema(
                type=openapi.TYPE_NUMBER, description="service price"
            ),
            "duration": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="service duration"
            ),
            "showed_name": openapi.Schema(
                type=openapi.TYPE_STRING, description="service name"
            ),
            "showed_description": openapi.Schema(
                type=openapi.TYPE_STRING, description="Service description"
            ),

        },
        required=["service_id", "price", "duration"],
    ),
    responses={
        200: BusinessServiceDetailsSerializer,
        400: openapi.Response(description="Invalid data provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(['PUT'])
def update_service_for_business(request, business_id):
    try:
        service_details_params = BusinessServiceDetailsParams(
            business_id=business_id,
            service_id=request.data['service_id'],
            price=request.data['price'],
            duration=request.data['duration'],
            showed_name=request.data['showed_name'],
            showed_description=request.data['showed_description'],
        )
        service_details_params.validate_details_to_update()
        result = business_service.update_service_for_business(service_details_params)
        return Response(data=result, status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method="delete",
    operation_description="Service delete endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "service_id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="service_id"
            ),
        },
        required=["service_id"],
    ),
    responses={
        200: openapi.TYPE_STRING,
        400: openapi.Response(description="Invalid data provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(['DELETE'])
def delete_service_for_business(request, business_id):
    try:
        service_details_params = BusinessServiceDetailsParams(
            business_id=business_id,
            service_id=request.data['service_id'],
        )
        service_details_params.validate_details_to_delete()
        return Response(data=business_service.delete_service_for_business(service_details_params), status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method="get",
    operation_description="Get business for service",
    responses={200: BusinessServiceDetailsSerializer(many=True)},
)
@api_view(["GET"])
def get_services_for_business(request, business_id: int) -> Response:
    return Response(data=business_service.get_services_for_business(business_id))


@swagger_auto_schema(
    method="post",
    operation_description="Business add employee endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "user_id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="user_id to add"
            ),
            "role": openapi.Schema(
                type=openapi.TYPE_STRING, description="Role of the employee, STAFF | ADMIN"
            ),
        },
        required=["user_id", "role"],
    ),
    responses={
        200: openapi.TYPE_STRING,
        400: openapi.Response(description="Invalid data provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["POST"])
def add_employee(request, business_id) -> Response:
    user_id, role = request.data['user_id'], request.data['role']
    return Response(data=business_service.add_employee(user_id=user_id, business_id=business_id, role=role))

@swagger_auto_schema(
    method="delete",
    operation_description="Business add employee endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "user_id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="user_id to add"
            ),
        },
        required=["user_id"],
    ),
    responses={
        200: openapi.TYPE_STRING,
        400: openapi.Response(description="Invalid data provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["DELETE"])
def remove_employee(request, business_id) -> Response:
    user_id= request.data['user_id']
    return Response(data=business_service.remove_employee(user_id, business_id))