from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from seller.models import Seller

class SellerAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            seller = Seller.objects.using('mysql_db').get(username=username)
            if seller and check_password(password, seller.password):
                return seller
        except Seller.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Seller.objects.using('mysql_db').get(pk=user_id)
        except Seller.DoesNotExist:
            return None
