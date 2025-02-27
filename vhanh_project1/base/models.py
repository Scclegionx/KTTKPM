# base/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class BaseUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'base_user'
