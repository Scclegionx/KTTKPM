from djongo import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('book', 'Book'),
        ('clothes', 'Clothes'),
        ('shoes', 'Shoes'),
        ('electronics', 'Electronics'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    seller_id = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return self.name
