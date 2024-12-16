from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers.userserializer import UserSerializer
from ..services.userservice import UserService

user_service = UserService()


@swagger_auto_schema(
    method='post',
    operation_description="User login endpoint",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
        },
        required=['email', 'password'],
    ),
    responses={
        200: UserSerializer,
        400: openapi.Response(description='Invalid email or password'),
    },
)
@api_view(['POST'])
def login_view(request) -> Response:
    email = request.data.get('email')
    password = request.data.get('password')
    user = user_service.login_user(request, email, password)
    if user is not None:
        return Response(user)
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    operation_description="User logout endpoint",
    responses={200: openapi.Response(description='Logged out successfully')},
)
@api_view(['POST'])
def logout_view(request) -> Response:
    user_service.logout_user(request)
    return Response({'success': 'Logged out successfully'})


@swagger_auto_schema(
    method='post',
    operation_description="User signup endpoint",
    request_body=UserSerializer,
    responses={
        201: openapi.Response(description='User created successfully!'),
        400: openapi.Response(description='Validation error'),
    },
)
@api_view(['POST'])
def signup_view(request) -> Response:
    data = request.data
    try:
        result = user_service.create_user(request, data)
        return Response(result, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Get all users",
    responses={200: UserSerializer(many=True)},
)
@api_view(['GET'])
def get_all(request) -> Response:
    users = user_service.get_all_users()
    return Response(users)


@swagger_auto_schema(
    method='get',
    operation_description="Get user by ID",
    manual_parameters=[
        openapi.Parameter(
            'user_id',
            openapi.IN_PATH,
            description="ID of the user",
            type=openapi.TYPE_INTEGER,
            required=True,
        )
    ],
    responses={
        200: UserSerializer,
        404: openapi.Response(description="User not found"),
    },
)
@api_view(['GET'])
def get_by_id(request, user_id: int) -> Response:
    try:
        user_data = user_service.get_user_by_id(user_id)
        return Response(user_data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_business_view(request) -> Response:
    try:
        business = user_service.create_business(request)
        return Response(business)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
