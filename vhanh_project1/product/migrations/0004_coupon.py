# Generated by Django 3.1.12 on 2025-02-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_clothes_electronics_shoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount_type', models.CharField(choices=[('percent', 'Percentage'), ('fixed', 'Fixed Amount')], max_length=10)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_type', models.CharField(choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'High'), ('vip', 'VIP')], max_length=10)),
                ('usage_limit', models.PositiveIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
            ],
            options={
                'db_table': 'coupon',
            },
        ),
    ]
