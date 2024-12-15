from django.urls import path

from .views.categoryview import add_category, remove_category, get_categories
from .views.serviceview import get_services, add_service, remove_service
from .views.userview import login_view, logout_view, signup_view, get_all, get_by_id, create_business_view
from .views.businessview import get_all_business, get_business_info, add_service_for_business, \
    delete_service_for_business, update_service_for_business

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
    ######################################################################################################
    path('category/get_all/', get_categories),
    path('category/add_category/', add_category),
    path('category/remove_category/', remove_category),
    ######################################################################################################
    path('service/get_all/', get_services),
    path('service/add_service/', add_service),
    path('service/remove_service/', remove_service),
]
