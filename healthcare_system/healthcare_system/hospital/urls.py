# urls.py
from django.urls import path
from .views import PatientSignupView,PatientLoginView

urlpatterns = [
    path('signup/', PatientSignupView.as_view(), name='patient_signup'),
     path('login/', PatientLoginView.as_view(), name='patient_login'),  # New login endpoint
]
