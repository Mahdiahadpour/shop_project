# Generated by Django 3.2.7 on 2021-10-15 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
