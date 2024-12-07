from django.urls import path
from .views.userview import login_view, logout_view, signup_view, get_all, get_by_id, create_business_view
from .views.businessview import get_all_business

urlpatterns = [
    path('user/login/', login_view),
    path('user/logout/', logout_view),
    path('user/signup/', signup_view),
    path('user/getall/', get_all),
    path('user/<int:user_id>/', get_by_id),
    path('user/createbusiness/', create_business_view),
    path('business/getall/', get_all_business)
]
