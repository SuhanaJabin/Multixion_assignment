# urls.py
from django.urls import path
from .views import PatientSignupView,PatientLoginView,PatientListView

urlpatterns = [
    path('signup/', PatientSignupView.as_view(), name='patient_signup'),
    path('login/', PatientLoginView.as_view(), name='patient_login'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
]
