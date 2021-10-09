from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(AbstractUser):
    email = models.EmailField()
    image = models.ImageField(upload_to='customers', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    ID_card_number = models.PositiveIntegerField(blank=True, null=True)
    date_entered = models.DateField(auto_now=True)
    mobile_number = models.CharField(max_length=11, unique=True)
    home_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#
# class Customer(AbstractUser):
#     email = models.EmailField(_('Email Address'), unique=True)
#     mobile = models.CharField(
#         verbose_name=_('Mobile Number'),
#         max_length=10,
#         unique=True,
#         blank=True, null=True,
#     )
#     profile_image = models.ImageField(
#         verbose_name=_("Profile Photo"),
#         upload_to="customer/user_images",
#         null=True, blank=True
#     )
#     amount_of_shopping = models.PositiveIntegerField(_('amount of shopping'), default=0)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     class Meta:
#         verbose_name = _("Customer")
#         verbose_name_plural = _("Customers")
#

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
