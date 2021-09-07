from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CostumerInfo(models.Model):
    costumer_user = models.ForeignKey(User, on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)


class CostumerAddress(models.Model):
    address_name = models.CharField(max_length=60)


class CostumerOrderHistory(models.Model):
    pass
