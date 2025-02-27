from djongo import models
from product.models import Product

class Electronics(Product):
    product_ptr = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    brand = models.CharField(max_length=100)
    warranty_period = models.CharField(max_length=50)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return f"{self.name} - {self.brand} - {self.warranty_period}"