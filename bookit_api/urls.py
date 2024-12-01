from django.urls import path
from .views.userview import login_view, logout_view, signup_view, get_all, get_by_id

urlpatterns = [
    path('user/login/', login_view),
    path('user/logout/', logout_view),
    path('user/signup/', signup_view),
    path('user/getall/', get_all),
    path('user/<int:user_id>/', get_by_id),
]
