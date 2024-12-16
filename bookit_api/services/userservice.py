from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from rest_framework.exceptions import ValidationError

from bookit_api.models import User
from bookit_api.serializers.userserializer import UserSerializer
# from bookit_api.services.bookingservice import BookingService
from bookit_api.services.businessuserservice import BusinessUserService


class UserService:
    def __init__(self):
        self.busines_user_service = BusinessUserService()
        # self.booking_service = BookingService()

    def login_user(self, request, email, password):
        """
        Authenticate and log in a user.
        """
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return UserSerializer(user).data
        raise ValidationError("Invalid email or password")

    def logout_user(self, request):
        """
        Log out the currently authenticated user.
        """
        if request.user.is_authenticated:
            logout(request)
            return {"success": "User logged out successfully"}
        raise ValidationError("No user is currently logged in")

    def create_user(self, request, data):
        """
        Create a new user and log them in immediately.
        """
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    email=data['email'],
                    password=data['password'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    phone_number=data['phone_number'],
                )
                login(request, user)
            return {"success": "User created successfully", "user": UserSerializer(user).data}
        except Exception as e:
            raise ValidationError(f"Failed to create user: {str(e)}")

    def get_all_users(self):
        """
        Retrieve all users.
        """
        users = User.objects.all()
        return UserSerializer(users, many=True).data

    def get_user_by_id(self, user_id):
        """
        Retrieve a user by their ID.
        """
        try:
            user = User.objects.get(pk=user_id)
            return UserSerializer(user).data
        except User.DoesNotExist:
            raise ValidationError(f"User with ID {user_id} not found")

    def create_business(self, request):
        """
        Create a business for the authenticated user.
        """
        if not request.user.is_authenticated:
            raise ValidationError("User must be authenticated to create a business")
        return self.busines_user_service.add_business_with_owner(request, request.user)

    def update_profile(self, user_id, data):
        """
        Update user profile information.
        """
        try:
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return {"success": "User profile updated successfully", "user": serializer.data}
        except User.DoesNotExist:
            raise ValidationError(f"User with ID {user_id} not found")
        except Exception as e:
            raise ValidationError(f"Failed to update profile: {str(e)}")

    def get_user(self, user_id: int):
        user = User.objects.get(pk=user_id)
        return user

    # def view_bookings(self, user_id: int):
    #     """
    #     Retrieve all bookings for a specific business.
    #     """
    #     try:
    #         bookings = self.booking_service.get_bookings_by_business(user_id)
    #         return bookings
    #     except Exception as e:
    #         raise ValidationError(f"Failed to retrieve bookings: {str(e)}")
    #
    # def update_availability(self, user_id, availability_data):
    #     """
    #     Placeholder for updating user availability (e.g., for employees).
    #     """
    #     pass
