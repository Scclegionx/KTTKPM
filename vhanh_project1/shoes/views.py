from rest_framework import viewsets
from .models import Shoes
from .serializers import ShoesSerializer

class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer