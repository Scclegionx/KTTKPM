from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(seller_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(seller_id=self.request.user.id)


# from product.models import Product
# from seller.models import Seller

# # Lấy seller1 từ MySQL
# seller1 = Seller.objects.using('mysql_db').filter(username='seller1').first()

# # Gán seller_id mặc định cho các bản ghi cũ
# if seller1:
#     Product.objects.filter(seller_id__isnull=True).update(seller_id=seller1.id)
