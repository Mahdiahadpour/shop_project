from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    category = models.OneToOneField(Category, on_delete=models.PROTECT)
