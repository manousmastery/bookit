from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import UserSerializer

class UserListView(APIView):
    def get(self, request):
        # Retrieve all Users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    