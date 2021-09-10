from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    sub_category = models.OneToOneField('self', on_delete=models.CASCADE, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    price_discount = models.PositiveIntegerField(null=True, blank=True)
    category = models.OneToOneField(Category, on_delete=models.PROTECT)
    size_choices = (
        ('extra small', 0),
        ('small', 1),
        ('medium', 2),
        ('large', 3),
        ('extra large', 4)
    )
    size = models.PositiveSmallIntegerField(choices=size_choices)
    color = models.CharField(max_length=25)
    unit_in_stock = models.PositiveIntegerField()
    ranking_choices = (
        ('Very Bad', 1),
        ('Bad', 2),
        ('Not Bad', 3),
        ('Good', 4),
        ('Very Good', 5),
    )
    ranking = models.PositiveIntegerField(choices=ranking_choices)
    image = models.ImageField(upload_to='media/product', blank=True, null=True)
