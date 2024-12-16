from rest_framework.exceptions import ValidationError

from bookit_api.models import Service
from bookit_api.models.servicecategory import ServiceCategory
from bookit_api.serializers.serviceserializer import ServiceSerializer
from bookit_api.services.businessservicedetailsservice import BusinessServiceDetailsService
from bookit_api.services.categoryservice import CategoryService


class ServiceService:
    def __init__(self):
        self.service_category_service = CategoryService()
        self.business_service_detail_service = BusinessServiceDetailsService()

    def add_service(self, service_name: str, category_name: str, description: str | None = None):
        if not self.service_category_service.is_category_exist(category_name):
            raise ValidationError(f"Category '{category_name}' does not exist.")

        category = ServiceCategory.objects.get(name=category_name)
        service = Service.objects.create(
            category=category,
            name=service_name,
            description=description,
        )
        return ServiceSerializer(service).data

    def remove_service(self, name: str):
        try:
            service = Service.objects.get(name=name)
            service.delete()
            return {"success": f"Service '{name}' has been removed."}
        except Service.DoesNotExist:
            raise ValidationError(f"Service '{name}' does not exist.")
        except Exception as e:
            raise ValidationError(f"Failed to remove service: {str(e)}")

    def update_service(self, service_id: int, name: str = None, description: str = None, category_name: str = None):
        try:
            service = Service.objects.get(id=service_id)

            if name:
                service.name = name
            if description:
                service.description = description
            if category_name:
                if not self.service_service.is_category_exist(category_name):
                    raise ValidationError(f"Category '{category_name}' does not exist.")
                service.category = ServiceCategory.objects.get(name=category_name)

            service.save()
            return ServiceSerializer(service).data
        except Service.DoesNotExist:
            raise ValidationError(f"Service with ID {service_id} does not exist.")
        except Exception as e:
            raise ValidationError(f"Failed to update service: {str(e)}")


    def get_all_services(self) -> list:
        services = Service.objects.all()
        return ServiceSerializer(services, many=True).data

    def is_service_exist(self, service_name: str) -> bool:
        return Service.objects.filter(name=service_name).exists()

    def get_service(self, service_id: int) -> Service:
        return Service.objects.get(service_id=service_id)

    def get_business_for_service(self, service_id: int):
        try:
            service = Service.objects.get(service_id=service_id)
            return self.business_service_detail_service.get_business_for_service(service)
        except Exception as e:
            raise e

    def get_services_from_category(self, category_name: str) -> list:
        category = self.service_category_service.get_category_from_name(category_name)
        services = Service.objects.filter(category=category).all()
        return services

    def get_business_details_from_service(self, category_name: str):
        services = self.get_services_from_category(category_name)
        business_details = self.business_service_detail_service.get_business_details_from_service(services)
        return business_details