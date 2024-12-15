from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..serializers.businessservicedetails import BusinessServiceDetailsSerializer
from ..serializers.servicecategoryserializer import ServiceCategorySerializer
from ..serializers.serviceserializer import ServiceSerializer
from ..services.serviceservice import ServiceService

service_service = ServiceService()


@swagger_auto_schema(
    method="get",
    operation_description="Get all services",
    responses={200: ServiceSerializer(many=True)},
)
@api_view(["GET"])
def get_services(request) -> Response:
    return Response(data=service_service.get_all_services())


@swagger_auto_schema(
    method="post",
    operation_description="Service add endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(
                type=openapi.TYPE_STRING, description="Service name"
            ),
            "description": openapi.Schema(
                type=openapi.TYPE_STRING, description="Service description"
            ),
        },
        required=["name", "description"],
    ),
    responses={
        200: ServiceCategorySerializer,
        400: openapi.Response(description="Invalid service provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["POST"])
def add_service(request) -> Response:
    service_data = request.data
    name = service_data.get("name", None)
    description = service_data.get("description", None)
    category_name = service_data.get("category", None)

    if not name or not category_name:
        raise ValidationError('"name" and "category" should be provided in the body')
    try:
        service = service_service.add_service(name, category_name, description)
        return Response(data=service, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@swagger_auto_schema(
    method="delete",
    operation_description="Category delete endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(
                type=openapi.TYPE_STRING, description="Category name"
            ),
        },
        required=["name"],
    ),
    responses={
        200: ServiceCategorySerializer,
        400: openapi.Response(description="Invalid category provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["DELETE"])
def remove_service(request) -> Response:
    service_name = request.data.get("name")
    if not service_name:
        raise ValidationError('"name" should be provided in the body')
    try:
        return Response(data=service_service.remove_service(service_name), status=status.HTTP_204_NO_CONTENT)
    except ValidationError as e:
        return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@swagger_auto_schema(
    method="get",
    operation_description="Get business for service",
    responses={200: openapi.Response("List of businesses", BusinessServiceDetailsSerializer(many=True))},
)
@api_view(["GET"])
def get_business_for_service(request, service_id: int) -> Response:
    return Response(data=service_service.get_business_for_service(service_id))
