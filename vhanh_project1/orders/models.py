from django.db import models
from cart.models import CartItem

class Order(models.Model):
    STATUS_CHOICES = [
        ('packing', 'Packing'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered'),
    ]

    customer_id = models.IntegerField()  # Lấy id từ customer MySQL
    items = models.ManyToManyField(CartItem)  # Gắn với CartItem trong PostgreSQL
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=255, default='') 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='packing')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'cart'
        db_table = 'order'

    def __str__(self):
        return f"Order {self.id} by Customer {self.customer_id}"