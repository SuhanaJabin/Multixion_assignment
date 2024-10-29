# urls.py
from django.urls import path
from .views import CheckPermissionView

urlpatterns = [
    path('check-permission/', CheckPermissionView.as_view(), name='check_permission'),
]
