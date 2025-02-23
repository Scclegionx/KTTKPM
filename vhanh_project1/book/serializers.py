from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    description = serializers.CharField()
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=100)
    rating = serializers.FloatField()

    def create(self, validated_data):
        return Book(**validated_data).save()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
