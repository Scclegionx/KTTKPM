from rest_framework import serializers
from cart.models import Cart, CartItem
from customer.models import Customer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        return CartItem.objects.using('cartdb').create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(using='cartdb')
        return instance


class CartSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.using('mysql_db').all()
    )
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        print(f"🚀 Creating Cart with data: {validated_data}")
        try:
            cart = Cart.objects.using('cartdb').create(**validated_data)
            print(f"✅ Created Cart: {cart}")
            return cart
        except Exception as e:
            print(f"❌ Error creating Cart: {e}")
            raise

    def update(self, instance, validated_data):
        print(f"🛠 Updating Cart with data: {validated_data}")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        try:
            instance.save(using='cartdb')
            print(f"✅ Updated Cart: {instance}")
            return instance
        except Exception as e:
            print(f"❌ Error updating Cart: {e}")
            raise
