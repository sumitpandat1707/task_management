from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Extra fields added to the default Django User model
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    role_choices = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('doctor_assistent', 'doctor_assistent'),
        ('tele_caller', 'tele_caller'),
        
    ]
    role = models.CharField(max_length=20, choices=role_choices, default='patient')
    
    def __str__(self):
        return self.username
