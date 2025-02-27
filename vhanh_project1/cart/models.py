# models.py (cart)
from django.db import models
from customer.models import Customer

class Cart(models.Model):
    customer_id = models.IntegerField()  # Lưu customer.id từ MySQL
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'cart'
        db_table = 'cart'

    def __str__(self):
        return f"Cart of customer {self.customer_id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # PostgreSQL
    product_id = models.CharField(max_length=24)  # MongoDB ObjectId (string)
    product_name = models.CharField(max_length=255, default='')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_ordered = models.BooleanField(default=False) 

    class Meta:
        app_label = 'cart'
        db_table = 'cart_item'

    def __str__(self):
        return f"{self.product_name} (x{self.quantity})"
