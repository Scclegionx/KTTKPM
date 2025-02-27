from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    CUSTOMER_TYPES = [
        ('low', 'Low'),
        ('mid', 'Mid'),
        ('high', 'High'),
        ('vip', 'VIP')
    ]

    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPES, default='low')

    groups = None
    user_permissions = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        app_label = 'customer'
        db_table = 'customer'