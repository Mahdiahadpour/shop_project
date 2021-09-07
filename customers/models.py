from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CostumerInfo(models.Model):
    costumer_user = models.ForeignKey(User, on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birthday = models.DateField()
    ID_card_number = models.PositiveSmallIntegerField(unique=True, max_length=10)
    E_mail = models.EmailField()


# going to be a form
class Address(models.Model):
    address_name = models.CharField(max_length=50)
    providence = models.CharField(max_length=16)
    city = models.CharField(max_length=35)
    address_detail = models.TextField()


class CostumerContactInfo(models.Model):
    mobile_number = models.CharField(max_length=11, null=False, unique=True)
    home_number = models.CharField(max_length=11)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)


class CostumerOrderHistory(models.Model):
    pass
