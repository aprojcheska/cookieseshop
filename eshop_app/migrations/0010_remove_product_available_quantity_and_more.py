# Generated by Django 4.2.3 on 2023-08-24 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0009_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_quantity',
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]