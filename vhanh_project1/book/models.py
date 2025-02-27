# book/models.py
from djongo import models
from product.models import Product

class Book(Product):
    product_ptr = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return f"{self.name} by {self.author}"
