from django.contrib.auth import authenticate, login, logout
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..models import User
from ..serializers.userserializer import UserSerializer


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
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    operation_description="User logout endpoint",
    responses={200: openapi.Response(description='Logged out successfully')},
)
@api_view(['POST'])
def logout_view(request) -> Response:
    logout(request)
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
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    try:
        user = User.objects.create_user(
            email=data['email'],
            password=request.data.get('password'),
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
        )
        login(request, user)  # Automatically log the user in
        return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='get',
    operation_description="Get all users",
    responses={200: UserSerializer(many=True)},
)
@api_view(['GET'])
def get_all(request) -> Response:
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


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
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)
