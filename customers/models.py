from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class Customer(AbstractUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birthday = models.DateField(null=True, blank=True)
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


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
