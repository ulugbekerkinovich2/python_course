from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basic_app.urls')),
    path('api-auth/', include('rest_framework.urls')),  # login - logout
    path('api/', include('dj_rest_auth.urls')),  # signin - signup
    path('api/v1/', include('second_app.urls')),
    path('api/register/', include('dj_rest_auth.registration.urls')),
]
