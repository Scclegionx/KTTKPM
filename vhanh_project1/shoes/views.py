from rest_framework import viewsets
from .models import Shoes
from .serializers import ShoesSerializer
from base.permissions import IsSellerOrReadOnly


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
    permission_classes = [IsSellerOrReadOnly]

    def get_queryset(self):
        return Shoes.objects.filter(seller_id=self.request.user.id)
