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
        """
        Add a new service under a specific category.

        :param service_name: name of the service.
        :param description: Description of the service.
        :param category_name: Name of the category to associate with the service.
        :return: Serialized service data.
        :raises ValidationError: If the category does not exist.
        """
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
        """
        Remove a service by its name.

        :param name: Name of the service to remove.
        :return: A success message on successful removal.
        :raises ValidationError: If the service does not exist.
        """
        try:
            service = Service.objects.get(name=name)
            service.delete()
            return {"success": f"Service '{name}' has been removed."}
        except Service.DoesNotExist:
            raise ValidationError(f"Service '{name}' does not exist.")
        except Exception as e:
            raise ValidationError(f"Failed to remove service: {str(e)}")

    def update_service(self, service_id: int, name: str = None, description: str = None, category_name: str = None):
        """
        Update an existing service's details.

        :param service_id: ID of the service to update.
        :param name: New name for the service (optional).
        :param description: New description for the service (optional).
        :param category_name: New category name for the service (optional).
        :return: Serialized service data.
        :raises ValidationError: If the service or category does not exist.
        """
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
        """
        Retrieves all services.

        :return: A list of all ServiceCategory instances.
        """
        services = Service.objects.all()
        return ServiceSerializer(services, many=True).data

    def is_service_exist(self, service_name: str) -> bool:
        """
        Checks if a category with the given name exists.

        :param service_name: Name of the category to check.
        :return: True if the category exists, otherwise False.
        """
        return Service.objects.filter(name=service_name).exists()

    def get_service(self, service_id: int) -> Service:
        return Service.objects.get(service_id=service_id)

    def get_business_for_service(self, service_id: int):
        try:
            service = Service.objects.get(service_id=service_id)
            return self.business_service_detail_service.get_business_for_service(service)
        except Exception as e:
            raise e
