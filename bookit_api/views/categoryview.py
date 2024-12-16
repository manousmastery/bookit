from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..serializers.servicecategoryserializer import ServiceCategorySerializer
from ..services.categoryservice import CategoryService

category_service = CategoryService()


@swagger_auto_schema(
    method="get",
    operation_description="Get all categories",
    responses={200: ServiceCategorySerializer(many=True)},
)
@api_view(["GET"])
def get_categories(request) -> Response:
    return Response(data=category_service.get_all_categories())


@swagger_auto_schema(
    method="post",
    operation_description="Category add endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, description="Category name"),
            "description": openapi.Schema(
                type=openapi.TYPE_STRING, description="Category description"
            ),
        },
        required=["name", "description"],
    ),
    responses={
        200: ServiceCategorySerializer,
        400: openapi.Response(description="Invalid category provided"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["POST"])
def add_category(request) -> Response:
    category_data = request.data
    try:
        category = category_service.add_category(category_data)
        return Response(data=category, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method="delete",
    operation_description="Category delete endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, description="Category name"),
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
def remove_category(request) -> Response:
    category_name = request.data.get("name")
    try:
        return Response(
            data=category_service.remove_category(category_name), status=status.HTTP_200_OK
        )
    except ValidationError as e:
        return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
