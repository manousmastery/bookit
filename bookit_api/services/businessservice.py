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

    def add(self, request, user):
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
                    owner=user,
                )
                BusinessUser.objects.create(
                    user=user,
                    business=business,
                    role='Owner'
                )
            return BusinessSerializer(business).data
        except Exception as e:
            raise ValidationError(f"Failed to create business: {str(e)}")

    def add_employee(self, request, user, business):
        """
        Add a user to a business with a specified role.
        """
        role = request.data.get('role')
        if not role:
            raise ValidationError('A role (Admin, Staff) must be provided')

        if role not in ['Admin', 'Staff']:
            raise ValidationError('Invalid role provided')

        try:
            with transaction.atomic():
                _ = BusinessUser.objects.create(
                    user=user,
                    business=business,
                    role=role
                )
            return {"success": f"User {user.email} added as {role} to business {business.name}."}
        except Exception as e:
            raise ValidationError(f"Failed to join business: {str(e)}")

    def remove_employee(self, business_id: int, user_id: int):
        """
        Remove an employee from a business.
        """
        try:
            business_user = BusinessUser.objects.get(business_id=business_id, user_id=user_id)
            business_user.delete()
            return {"success": f"User with ID {user_id} removed from business with ID {business_id}."}
        except BusinessUser.DoesNotExist:
            raise ValidationError(f"Employee with User ID {user_id} not found in Business ID {business_id}.")
        except Exception as e:
            raise ValidationError(f"Failed to remove employee: {str(e)}")

    def get_employees(self, business_id: int):
        """
        Retrieve all employees of a business.
        """
        try:
            business_users = BusinessUser.objects.filter(business_id=business_id)
            users = User.objects.filter(id__in=business_users.values_list('user_id', flat=True))
            return UserSerializer(users, many=True).data
        except Exception as e:
            raise ValidationError(f"Failed to retrieve employees: {str(e)}")

    def get_business_info(self, business_id: int):
        """
        Retrieve detailed information of a business, including its employees.
        """
        try:
            business = Business.objects.get(business_id=business_id)
            employees = self.get_employees(business_id)
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
