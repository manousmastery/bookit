from bookit_api.helpers import BusinessServiceDetailsParams
from bookit_api.models import BusinessServiceDetails
from bookit_api.serializers.businessservicedetails import BusinessServiceDetailsSerializer


class BusinessServiceDetailsService:
    def add_business_service_details(self, business_detail_service_params: BusinessServiceDetailsParams):
        try:
            business_service_detail = BusinessServiceDetails.objects.create(
                business=business_detail_service_params.business,
                service=business_detail_service_params.service,
                price=business_detail_service_params.price,
                duration=business_detail_service_params.duration,
                showed_name=business_detail_service_params.showed_name or business_detail_service_params.service.name,  # Default to the service's name if no custom name is provided
                showed_description=business_detail_service_params.showed_description or business_detail_service_params.service.description  # Default to the service's description
            )
            return BusinessServiceDetailsSerializer(business_service_detail).data
        except not BusinessServiceDetails.DoesNotExist:
            raise ValueError("The provided business service association already exist.")
        except Exception as e:
            raise e

    def update_business_service(self, business_detail_service_params: BusinessServiceDetailsParams):
        try:
            business_detail_service_params.validate_details_to_update()
            business_service_detail = BusinessServiceDetails.objects.filter(
                business=business_detail_service_params.business,
                service=business_detail_service_params.service
            ).first()

            if business_detail_service_params.price is not None:
                business_service_detail.price = business_detail_service_params.price
            if business_detail_service_params.duration is not None:
                business_service_detail.duration = business_detail_service_params.duration
            if business_detail_service_params.showed_name is not None:
                business_service_detail.showed_name = business_detail_service_params.showed_name
            if business_detail_service_params.showed_description is not None:
                business_service_detail.showed_description = business_detail_service_params.showed_description

            business_service_detail.save()

            return BusinessServiceDetailsSerializer(business_service_detail).data

        except BusinessServiceDetails.DoesNotExist:
            raise ValueError("The provided service does not exist for this business.")
        except Exception as e:
            raise Exception(f"An error occurred while updating the business service: {str(e)}")

    def delete_business_service(self, business_detail_service_params: BusinessServiceDetailsParams):
        try:
            business_service_detail = BusinessServiceDetails.objects.get(
                business=business_detail_service_params.business,
                service=business_detail_service_params.service
            )
            business_service_detail.delete()
            return {
                "success": f"Service with ID {business_detail_service_params.service.name} successfully removed from business with ID {business_detail_service_params.business.name}."}
        except BusinessServiceDetails.DoesNotExist:
            raise ValueError(
                f"Business service combination with business ID {business_detail_service_params.business.business_id} and service ID {business_detail_service_params.service.service_id} does not exist.")

        except Exception as e:
            raise Exception(f"An error occurred while deleting the business service: {str(e)}")

    def get_services_for_business(self, business):
        try:
            service_details = BusinessServiceDetails.objects.filter(business=business)
            return BusinessServiceDetailsSerializer(service_details, many=True).data
        except Exception as e:
            raise e

    def get_business_for_service(self, service):
        try:
            business_services = BusinessServiceDetails.objects.filter(service=service)
            return BusinessServiceDetailsSerializer(business_services, many=True).data
        except Exception as e:
            raise e
