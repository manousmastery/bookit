from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import UserSerializer

class UserGetView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id',  # The name of the parameter
                openapi.IN_PATH,  # Location of the parameter
                description="Id of the user",  # Description shown in Swagger
                type=openapi.TYPE_STRING,  # Data type
            )
        ]
    )
    def get(self, request, id=None):
        if id:
            # Retrieve a single User
            try:
                user = User.objects.get(pk=id)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data)
    
class UserCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=UserSerializer,  # Specifies the expected request body schema
        manual_parameters=[]
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)