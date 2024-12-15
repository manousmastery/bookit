from django.core.exceptions import ValidationError

from bookit_api.helpers import BusinessServiceDetailsParams
from bookit_api.models import Business
from bookit_api.serializers.businessserializer import BusinessSerializer
from bookit_api.services.businessservicedetailsservice import BusinessServiceDetailsService
from bookit_api.services.businessuserservice import BusinessUserService
from bookit_api.services.serviceservice import ServiceService
from bookit_api.services.userservice import UserService


class BusinessService:
    def __init__(self):
        self.business_user_service = BusinessUserService()
        self.service_service = ServiceService()
        self.business_service_detail_service = BusinessServiceDetailsService()
        self.user_service = UserService()

    def get_all(self):
        businesses = Business.objects.all()
        return BusinessSerializer(businesses, many=True).data

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

    def get_services_for_business(self, business_id: int):
        try:
            business = Business.objects.get(business_id=business_id)
            return self.business_service_detail_service.get_services_for_business(business)
        except Exception as e:
            raise e

    def add_employee(self, user_id, business_id, role: str):
        try:
            user = self.user_service.get_user(user_id)
            business = Business.objects.get(business_id=business_id)
            return self.business_user_service.add_employee(user=user, business=business, role=role)
        except Exception as e:
            raise e
        # (f"Failed to join business: {str(e)}")

    def remove_employee(self, user_id, business_id):
        try:
            return self.business_user_service.remove_employee(business_id, user_id)
        except Exception as e:
            raise e
