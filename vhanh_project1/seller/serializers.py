from rest_framework import serializers
from seller.models import Seller

class SellerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Seller
        fields = ('username', 'password', 'shop_name')

    def create(self, validated_data):
        return Seller.objects.db_manager('mysql_db').create_user(**validated_data)

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'username', 'shop_name', 'is_verified')