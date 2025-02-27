from django.contrib.auth.models import AbstractUser
from django.db import models

class Seller(AbstractUser):
    shop_name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    groups = None  # Bỏ groups
    user_permissions = None  # Bỏ user_permissions

    class Meta:
        app_label = 'customer'
        db_table = 'seller'
