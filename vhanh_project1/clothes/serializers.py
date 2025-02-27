# # clothes/serializers.py
# from rest_framework import serializers
# from .models import Clothes

# class ClothesSerializer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField(allow_blank=True, required=False)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     stock = serializers.IntegerField(min_value=0)
#     size = serializers.CharField(max_length=10)
#     color = serializers.CharField(max_length=50)
#     created_at = serializers.DateTimeField(required=False)
#     updated_at = serializers.DateTimeField(required=False)

#     def create(self, validated_data):
#         return Clothes.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         for field, value in validated_data.items():
#             setattr(instance, field, value)
#         instance.save()
#         return instance


from rest_framework import serializers
from .models import Clothes

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'