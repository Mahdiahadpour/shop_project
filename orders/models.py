from django.db import models

# Create your models here.
from customers.models import Customer
from product.models import Product


class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    fulfilled = models.BooleanField(default=False)
    fulfilled_time = models.DateField()
    order_date = models.DateTimeField()
    costumer_massage = models.TextField()


class Payment(models.Model):
    payment_type_choices = (
        ('Online', 1),
        ('On deliver', 2)
    )
    payment_type = models.PositiveSmallIntegerField(choices=None)
    payed = models.BooleanField(default=False)


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_detail = models.OneToOneField(OrderDetails, on_delete=models.PROTECT)
    deleted = models.BooleanField(default=False)
