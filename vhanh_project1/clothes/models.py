from djongo import models
from product.models import Product

# Clothes Model
class Clothes(Product):
    product_ptr = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    size = models.CharField(max_length=10) 
    color = models.CharField(max_length=50)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return f"{self.name} - {self.size} - {self.color}"