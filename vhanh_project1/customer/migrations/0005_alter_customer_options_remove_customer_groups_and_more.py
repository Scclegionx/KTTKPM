# Generated by Django 4.2.19 on 2025-02-24 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_options_alter_customer_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_permissions',
        ),
    ]
