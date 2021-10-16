from django.db import models
from django.utils.translation import gettext_lazy as _
from shop_project import settings
from customers.models import Customer, Address
from product.models import Product


# Create your models here.


class Discount(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='discounts')
    created = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    amount = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = _('discounts')
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')

    def __str__(self):
        return f'{self.customer} {self.amount}%'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name}'


class Payment(models.Model):
    payment_type_choices = (('Online', 1), ('On deliver', 2))
    payment_type = models.PositiveSmallIntegerField(choices=None)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return 'payment'


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_detail = models.ManyToManyField(OrderItem)
    deleted = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False, editable=False)
    fulfilled_time = models.DateField(auto_now_add=True, editable=False)
    costumer_massage = models.TextField()
    # shipment_method = models.ForeignKey('Shipment', on_delete=models.PROTECT)
    # shipment_price = models.PositiveIntegerField(editable=False)
    total = models.PositiveIntegerField(null=True,editable=False)
    address = models.ForeignKey(Address,null=True, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'order'

    def save(self, *args, **kwargs) -> None:
        for item in self.order_detail.all():
            product = item.product
            self.total += (product.price -
                           product.price_discount) * item.quantity
            # self.total += self.shipment_method.price
        return super().save()


class Shipment(models.Model):
    # order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shipment_statues = models.CharField(max_length=100)
    shipper = models.CharField(max_length=100)
    shipper_phone = models.CharField(max_length=11)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.shipment_statues
