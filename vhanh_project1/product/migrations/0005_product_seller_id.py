# Generated by Django 3.1.12 on 2025-02-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
