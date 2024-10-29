# main project's urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),              # Admin interface
    path('api/', include('healthcare_system.hospital.urls')),       # Include app URLs for the signup endpoint
]
