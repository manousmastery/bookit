from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers.businessserializer import BusinessSerializer
from ..services.businessservice import BusinessService

business_service =  BusinessService()

@swagger_auto_schema(
    method='get',
    operation_description="Get all business",
    responses={200: BusinessSerializer(many=True)},
)
@api_view(['GET'])
def get_all_business(request) -> Response:
    business = business_service.get_all()
    return BusinessSerializer(business, many=True).data

