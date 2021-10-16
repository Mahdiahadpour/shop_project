from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _



class Customer(AbstractUser):
    email = models.EmailField()
    image = models.ImageField(upload_to='customers', blank=True, null=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birthday = models.DateField()
    ID_card_number = models.PositiveIntegerField(unique=True)
    date_entered = models.DateField(auto_now=True)
    mobile_number = models.CharField(max_length=11, unique=True)
    home_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# going to be a form
class Address(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    address_name = models.CharField(max_length=50)
    providence = models.CharField(max_length=16)
    # use library
    city = models.CharField(max_length=35)
    postal_code = models.PositiveSmallIntegerField()
    # address with choice must be added
    address_detail = models.TextField()

    def __str__(self):
        return f'{self.address_name}'
