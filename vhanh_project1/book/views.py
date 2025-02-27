# book/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from base.permissions import IsSellerOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsSellerOrReadOnly]

    def get_queryset(self):
        return Book.objects.filter(seller_id=self.request.user.id)