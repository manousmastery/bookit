from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Business
from ..serializers import BusinessSerializer


class BusinessListView(APIView):
    def get(self, request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)  # Serialize queryset
        return Response(serializer.data)  # Return serialized data
