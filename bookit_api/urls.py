from django.urls import path

from .views.bookingview import create_booking, cancel_booking, update_booking, get_booking, get_booking_by_business, \
    get_booking_by_client, get_booking_by_employee
from .views.categoryview import add_category, remove_category, get_categories
from .views.serviceview import get_services, add_service, remove_service, get_business_for_service
from .views.userview import login_view, logout_view, signup_view, get_all, get_by_id, create_business_view
from .views.businessview import get_all_business, get_business_info, add_service_for_business, \
    delete_service_for_business, update_service_for_business, get_services_for_business, add_employee, remove_employee, \
    get_business_from_category

urlpatterns = [
    path('user/login/', login_view),
    path('user/logout/', logout_view),
    path('user/signup/', signup_view),
    path('user/getall/', get_all),
    path('user/<int:user_id>/', get_by_id),
    path('user/createbusiness/', create_business_view),

    ######################################################################################################

    path('business/get_all/', get_all_business),
    path('business/<int:business_id>/', get_business_info),
    path('business/add_service/<int:business_id>/', add_service_for_business),
    path('business/update_service/<int:business_id>/', update_service_for_business),
    path('business/delete_service/<int:business_id>/', delete_service_for_business),
    path('business/services/<int:business_id>/', get_services_for_business),
    path('business/add_employee/<int:business_id>/', add_employee),
    path('business/remove_employee/<int:business_id>/', remove_employee),
    path('business/get_by_category/', get_business_from_category),

    ######################################################################################################
    path('category/get_all/', get_categories),
    path('category/add_category/', add_category),
    path('category/remove_category/', remove_category),

    ######################################################################################################

    path('service/get_all/', get_services),
    path('service/add_service/', add_service),
    path('service/remove_service/', remove_service),
    path('service/business/<int:service_id>/', get_business_for_service),

    ######################################################################################################

    path('booking/create/', create_booking),
    path('booking/cancel/<int:booking_id>', cancel_booking),
    path('booking/update/<int:booking_id>', update_booking),
    path('booking/get/<int:booking_id>', get_booking),
    path('booking/business/<int:business_id>', get_booking_by_business),
    path('booking/client/', get_booking_by_client),
    path('booking/employee/', get_booking_by_employee),
]
