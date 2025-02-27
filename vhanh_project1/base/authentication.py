# base/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from customer.models import Customer
from seller.models import Seller
from django.contrib.auth import get_user_model

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get("user_id")
        backend = validated_token.get("backend")  # Lấy backend từ token
        
        try:
            if backend == 'customer.backends.CustomerAuthBackend':
                return Customer.objects.using('mysql_db').get(id=user_id)
            elif backend == 'seller.backends.SellerAuthBackend':
                return Seller.objects.using('mysql_db').get(id=user_id)
            else:
                return get_user_model().objects.get(id=user_id)
        except Exception:
            return None