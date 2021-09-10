from django.db import models

# Create your models here.
from customers.models import Customer, Address
from product.models import Product


class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    fulfilled = models.BooleanField(default=False, editable=False)
    fulfilled_time = models.DateField(editable=False)
    order_date = models.DateTimeField(editable=False)
    costumer_massage = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    shipment_method = models.CharField(max_length=100)
    shipment_price = models.PositiveIntegerField()


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


class Shipment(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shipment_statues = models.CharField(max_length=100)
    shipper = models.CharField(max_length=100)
    shipper_phone = models.CharField(max_length=11)
