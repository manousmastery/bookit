from django.core.exceptions import ValidationError
from django.db import transaction

from bookit_api.models import BusinessUser, Business, User
from bookit_api.serializers.userserializer import UserSerializer


class BusinessUserService:
    def get(self, business_id: int):
        return BusinessUser.objects.filter(business=business_id)

    def add_owner_to_business(self, user: User, business: Business, role: str | None = None):
        BusinessUser.objects.create(
            user=user,
            business=business,
            role=role or 'STAFF'
        )

    def add_employee(self,  user, business, role: str | None = None):
        """
        Add a user to a business with a specified role.
        """
        if role == 'Owner':
            raise ValidationError('Invalid role provided')

        try:
            with transaction.atomic():
                _ = BusinessUser.objects.create(
                    user=user,
                    business=business,
                    role=role or 'STAFF'
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
