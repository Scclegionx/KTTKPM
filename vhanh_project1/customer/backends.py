# customer/backends.py
from django.contrib.auth.backends import ModelBackend
from customer.models import Customer

class CustomerAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Customer.objects.using('mysql_db').get(username=username)
            if user and user.check_password(password):
                return user
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.using('mysql_db').get(pk=user_id)
        except Customer.DoesNotExist:
            return None
