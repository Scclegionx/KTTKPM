from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    # Các field khác của Customer

    # Thêm related_name để tránh trùng với auth.User
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customer_groups",  # 👈 Thêm related_name để tránh conflict
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customer_permissions",  # 👈 Thêm related_name để tránh conflict
        blank=True,
        help_text="Specific permissions for this user.",
    )
