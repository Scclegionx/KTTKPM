from rest_framework import viewsets
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.using('cartdb').all()
    serializer_class = CartSerializer

    def get_queryset(self):
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            return Cart.objects.using('cartdb').filter(customer_id=customer_id)
        return Cart.objects.using('cartdb').all()


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.using('cartdb').all()
    serializer_class = CartItemSerializer