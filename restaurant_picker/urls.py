"""restaurant_picker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from api.views import admin_logout
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
    title="Restaurant Picker API",
    default_version='v1',
    description="Not Available.",
    terms_of_service="https://rp.com/",
    contact=openapi.Contact(email="Nahidjahid8698@gmail.com"),
    license=openapi.License(name="Private License"),
  ),
  public=True,
  permission_classes=(permissions.IsAdminUser,)
)

urlpatterns = [
    url(r'^$', login_required(function=schema_view.with_ui('swagger', cache_timeout=0), login_url='/admin/login/?next=/'), name='schema-swagger-ui'),
    url('admin/', admin.site.urls),
    url('api/v1/', include('api.urls')),
    url(r'^(?P<format>\.json|\.yaml)$', login_required(function=schema_view.without_ui(cache_timeout=0), login_url='/admin/login/?next=/'), name='schema-json'),
    url(r'^redoc/$', login_required(function=schema_view.with_ui('redoc', cache_timeout=0), login_url='/admin/login/?next=/'), name='schema-redoc'),
    path('accounts/logout/', admin_logout),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
