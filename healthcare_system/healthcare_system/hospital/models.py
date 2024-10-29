from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Custom User model with roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')  # Default role set to 'patient'

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='hospital_user_set',  # Unique related name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='hospital_user_set',  # Unique related name
        blank=True,
    )

    def __str__(self):
        return f"{self.username} - {self.role}"

# Patient model with additional patient information
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    age = models.PositiveIntegerField(blank=True, null=True)
    blood_group = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ])
    phone_no = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Patient"
