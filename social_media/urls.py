"""
URL configuration for social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),

    # jwt path

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),




]

api_path = [
path('api/v0/user/' , include('apps.users.api.v0.urls')),
path('api/v0/post/' , include('apps.post.api.v0.urls')),
path('api/v0/follower/' , include('apps.follower.api.v0.urls')),
path('api/v0/chat/' , include('apps.chat.api.v0.urls')),
path('api/v0/notification/' , include('apps.notification.api.v0.urls')),
]
urlpatterns += api_path


schema_view = get_schema_view(
   openapi.Info(
      title="Social Media API",
      default_version='v0',
      description="Social Media test",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_path = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += swagger_path


