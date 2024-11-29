from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Business
from ..serializers import BusinessSerializer


class BusinessView(APIView):
    def get(self, request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)  # Serialize queryset
        return Response(serializer.data)  # Return serialized data
    
    @swagger_auto_schema(
        request_body=BusinessSerializer  # Specifies the expected request body schema
    )
    def post(self, request):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)