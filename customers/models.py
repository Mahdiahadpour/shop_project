from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    image = models.ImageField(upload_to='media/customers', blank=True, null=True)

    role = (
        (1, 'admin'),
        (2, 'staff'),
        (3, 'customer'),
    )
    user_role = models.SmallIntegerField(choices=role, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class CostumerInfo(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birthday = models.DateField()
    ID_card_number = models.PositiveIntegerField(unique=True)
    E_mail = models.EmailField()
    date_entered = models.DateField(editable=False, auto_now=True)


# going to be a form
class Address(models.Model):
    address_name = models.CharField(max_length=50)
    providence = models.CharField(max_length=16)
    # use library
    city = models.CharField(max_length=35)
    postal_code = models.PositiveSmallIntegerField()
    # address with choice must be added
    address_detail = models.TextField()


# must be edited
class CostumerContactInfo(models.Model):
    mobile_number = models.CharField(max_length=11, null=False, unique=True)
    home_number = models.CharField(max_length=11)


class Customer(models.Model):
    costumer_user = models.OneToOneField(User, on_delete=models.RESTRICT)
    costumer_info = models.OneToOneField(CostumerInfo, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    costumer_contact = models.OneToOneField(CostumerContactInfo, on_delete=models.PROTECT)
