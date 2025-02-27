from djongo import models
from product.models import Product

# Shoes Model
class Shoes(Product):
    product_ptr = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    size = models.IntegerField()  # Shoe size
    material = models.CharField(max_length=100)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return f"{self.name} - Size {self.size} - {self.material}"