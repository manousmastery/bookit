from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Q

from bookit_api.models import Business, BusinessUser, User
from bookit_api.serializers.businessserializer import BusinessSerializer
from bookit_api.serializers.userserializer import UserSerializer
from bookit_api.services.businessuserservice import BusinessUserService


class BusinessService:
    def __init__(self):
        self.business_user_service = BusinessUserService()

    def get_all(self):
        """
        Retrieve all businesses with their serialized data.
        """
        businesses = Business.objects.all()
        return BusinessSerializer(businesses, many=True).data

    def add_business_with_owner(self, request, user):
        """
        Add a new business and assign the creator as the owner.
        """
        serializer = BusinessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                business = Business.objects.create(
                    name=serializer.validated_data['name'],
                    description=serializer.validated_data.get('description'),
                    latitude=serializer.validated_data.get('latitude', None),
                    longitude=serializer.validated_data.get('longitude', None),
                    address=serializer.validated_data.get('address', None),
                )
                self.business_user_service.add_owner_to_business(
                    user=user,
                    business=business,
                    role='Owner'
                )
            return BusinessSerializer(business).data
        except Exception as e:
            raise ValidationError(f"Failed to create business: {str(e)}")


    def get_business_info(self, business_id: int):
        """
        Retrieve detailed information of a business, including its employees.
        """
        try:
            business = Business.objects.get(business_id=business_id)
            employees = self.business_user_service.get_employees(business_id)
            business_data = BusinessSerializer(business).data
            business_data['employees'] = employees
            return business_data
        except Business.DoesNotExist:
            raise ValidationError(f"Business with ID {business_id} not found")
        except Exception as e:
            raise ValidationError(f"Failed to retrieve business info: {str(e)}")

    def get_business_by_filter(self, filter: str):
        """
        Retrieve businesses matching a name filter.
        """
        try:
            businesses = Business.objects.filter(Q(name__icontains=filter) | Q(description__icontains=filter))
            return BusinessSerializer(businesses, many=True).data
        except Exception as e:
            raise ValidationError(f"Failed to filter businesses: {str(e)}")
