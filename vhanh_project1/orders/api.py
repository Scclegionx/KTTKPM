# seller/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Lọc danh sách order chưa thanh toán
    @action(detail=False, methods=['get'], url_path='unpaid')
    def unpaid_orders(self, request):
        unpaid_orders = Order.objects.filter(is_paid=False)
        serializer = self.get_serializer(unpaid_orders, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='paid')
    def paid_orders(self, request):
        paid_orders = Order.objects.filter(is_paid=True)
        serializer = self.get_serializer(paid_orders, many=True)
        return Response(serializer.data)

    # Xác nhận thanh toán
    @action(detail=True, methods=['patch'], url_path='confirm-payment')
    def confirm_payment(self, request, pk=None):
        try:
            order = self.get_object()
            if order.is_paid:
                return Response({'message': 'Order đã được thanh toán'}, status=status.HTTP_400_BAD_REQUEST)

            order.is_paid = True
            order.status = 'delivered'
            order.save()
            return Response({'message': 'Order đã được xác nhận thanh toán'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error': 'Order không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
