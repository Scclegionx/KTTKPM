# from rest_framework import serializers
# from .models import Electronics


# class ElectronicsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Electronics
#         fields = '__all__'


# electronics/serializers.py
import json
from django.core.exceptions import ValidationError
from .models import Electronics

class ElectronicsSerializer:
    """Chuyển đổi giữa Electronics object và JSON"""

    @staticmethod
    def serialize(electronic):
        """Object -> JSON"""
        return {
            'id': electronic.id,
            'name': electronic.name,
            'description': electronic.description,
            'price': str(electronic.price),  # Decimal -> string
            'stock': electronic.stock,
            'brand': electronic.brand,
            'warranty_period': electronic.warranty_period,
        }

    @staticmethod
    def deserialize(data):
        """JSON -> Object"""
        try:
            return {
                'name': data['name'],
                'description': data['description'],
                'price': data['price'],
                'stock': data['stock'],
                'brand': data['brand'],
                'warranty_period': data['warranty_period'],
            }
        except KeyError as e:
            raise ValidationError(f"Thiếu trường bắt buộc: {e}")
