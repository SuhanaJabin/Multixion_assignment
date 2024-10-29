# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# User model with roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# Patient model with specific information for each patient
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    medical_history = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Patient"

# Doctor model with patient management functionality
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    patients = models.ManyToManyField(Patient, blank=True, related_name="assigned_doctors")

    def __str__(self):
        return f"{self.user.username} - Doctor"
