from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('superAdmin', 'Super Admin'),
        ('supervisor', 'Supervisor'),
        ('agence', 'Agence'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)

    # Add related_name to the groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups',  # Unique related_name
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',  # Unique related_name
        help_text='Specific permissions for this user.'
    )
    
    
class Zone(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Agency(models.Model):
    TYPE_CHOICES = (
        ('bureau', 'Bureau'),
        ('agent', 'Agent'),
    )
    type         = models.CharField(max_length=6, choices=TYPE_CHOICES)
    zone         = models.ForeignKey(Zone, related_name='agencies', on_delete=models.CASCADE)
    category     = models.ForeignKey(Category, related_name='agencies', on_delete=models.CASCADE)
    status       = models.BooleanField(default=True)
    logo         = models.ImageField(upload_to='logos/')
    nomination   = models.CharField(max_length=100)
    responsable  = models.CharField(max_length=100)
    adresse      = models.CharField(max_length=255)
    tel_portable = models.CharField(max_length=20)
    tel_bureau   = models.CharField(max_length=20)
    agence_confiance = models.BooleanField(default=False)
    cne_cin      = models.CharField(max_length=20)
