from djongo import models

class Coupon(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('percent', 'Percentage'),
        ('fixed', 'Fixed Amount')
    ]

    CUSTOMER_TYPES = [
        ('low', 'Low'),
        ('mid', 'Mid'),
        ('high', 'High'),
        ('vip', 'VIP')
    ]

    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPES)
    usage_limit = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    class Meta:
        app_label = 'product'
        db_table = 'coupon'

    def __str__(self):
        return f"{self.code} ({self.customer_type})"
