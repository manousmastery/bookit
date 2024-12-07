from django.shortcuts import redirect
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Bookit API",
        default_version='v1',
        description="API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('bookit_api.urls')),  # Delegate to `bookit_api/urls.py`
    path('', lambda request: redirect('schema-swagger-ui', permanent=False)),  # Redirect root URL to Swagger UI
]
