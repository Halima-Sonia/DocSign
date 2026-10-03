from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('staff', 'Staff'),
        ('patient', 'Patient'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='patient'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username


class PatientProfile(models.Model):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    blood_group = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    emergency_contact = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    medical_history = models.TextField(
        blank=True,
        null=True
    )

    allergies = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username}'s Patient Profile"