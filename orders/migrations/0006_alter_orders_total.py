# Generated by Django 3.2.7 on 2021-10-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orders_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
