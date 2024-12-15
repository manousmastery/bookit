from django.core.exceptions import ValidationError
from django.db import transaction

from bookit_api.helpers import BusinessServiceDetailsParams
from bookit_api.models import Business
from bookit_api.serializers.businessserializer import BusinessSerializer
from bookit_api.services.businessservicedetailsservice import BusinessServiceDetailsService
from bookit_api.services.businessuserservice import BusinessUserService
from bookit_api.services.serviceservice import ServiceService


class BusinessService:
    def __init__(self):
        self.business_user_service = BusinessUserService()
        self.service_service = ServiceService()
        self.business_service_detail_service = BusinessServiceDetailsService()

    def get_all(self):
        businesses = Business.objects.all()
        return BusinessSerializer(businesses, many=True).data

    def add_business_with_owner(self, request, user):
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

    def add_service_for_business(self, business_detail_service_params: BusinessServiceDetailsParams):
        try:
            business_detail_service_params.business = Business.objects.get(business_id=business_detail_service_params.business_id)
            business_detail_service_params.service = self.service_service.get_service(business_detail_service_params.service_id)

            business_service_details = self.business_service_detail_service.add_business_service_details(
                business_detail_service_params
            )
            return business_service_details
        except Exception as e:
            raise ValidationError(f"Failed to create business service detail: {str(e)}")

    def update_service_for_business(self, business_detail_service_params: BusinessServiceDetailsParams):
        try:
            business_detail_service_params.business = Business.objects.get(business_id=business_detail_service_params.business_id)
            business_detail_service_params.service = self.service_service.get_service(business_detail_service_params.service_id)

            business_service_details = self.business_service_detail_service.update_business_service(
                business_detail_service_params
            )
            return business_service_details
        except Exception as e:
            raise ValidationError(f"Failed to update business service details: {str(e)}")

    def delete_service_for_business(self, business_detail_service_params: BusinessServiceDetailsParams):
        try:
            business_detail_service_params.business = Business.objects.get(business_id=business_detail_service_params.business_id)
            business_detail_service_params.service = self.service_service.get_service(business_detail_service_params.service_id)
            return self.business_service_detail_service.delete_business_service(business_detail_service_params)
        except Exception as e:
            raise ValidationError(f"Failed to delete business service detail: {str(e)}")

    # def get_business_by_filter(self, filter: str):
    #     try:
    #         businesses = Business.objects.filter(Q(name__icontains=filter) | Q(description__icontains=filter))
    #         return BusinessSerializer(businesses, many=True).data
    #     except Exception as e:
    #         raise ValidationError(f"Failed to filter businesses: {str(e)}")

    #
    # def is_business_exist(self, business_id: int) -> bool:
    #     """
    #     Checks if a category with the given name exists.
    #
    #     :param service_name: Name of the category to check.
    #     :return: True if the category exists, otherwise False.
    #     """
    #     return Business.objects.filter(business_id=business_id).exists()

