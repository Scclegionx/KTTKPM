from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from base.models import BaseUser

admin.site.register(BaseUser, UserAdmin)
