# Generated by Django 3.1.12 on 2025-02-26 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20250225_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'High'), ('vip', 'VIP')], default='low', max_length=10),
        ),
    ]
