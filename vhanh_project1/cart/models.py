from django.db import models
from customer.models import Customer
from bson import ObjectId
from book.models import Book

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Cart {self.id} for {self.customer.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book_id = models.CharField(max_length=24)  # Lưu ObjectId từ MongoDB
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def get_book(self):
        """Truy vấn MongoDB lấy thông tin Book theo book_id."""
        try:
            return Book.objects.get(id=ObjectId(self.book_id))
        except Book.DoesNotExist:
            return None

    def subtotal(self):
        """Tính tổng tiền dựa vào thông tin sách trong MongoDB."""
        book = self.get_book()
        return self.quantity * float(book.price) if book else 0

    def __str__(self):
        book = self.get_book()
        return f"{self.quantity} x {book.title}" if book else "Book not found"
