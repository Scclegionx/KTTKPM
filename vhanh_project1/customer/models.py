from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    email = models.EmailField(unique=True)  
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "username"  
    REQUIRED_FIELDS = ["email"]  
    

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customer_groups",  
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customer_permissions",  
        blank=True,
        help_text="Specific permissions for this user.",
    )
