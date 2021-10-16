from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    sub_category = models.ForeignKey('self',
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    price_discount = models.PositiveIntegerField(null=True, blank=True)
    size_choices = (('extra small', 'extras small'), ('small', 'small'),
                    ('medium', 'medium'), ('large', 'large'), ('extra large',
                                                               'extra large'))
    size = models.CharField(max_length=30, choices=size_choices)
    color = models.CharField(max_length=25)
    unit_in_stock = models.PositiveIntegerField()
    ranking_choices = (
        ('Very Bad', 'Very Bad'),
        ('Bad', 'Bad'),
        ('Not Bad', 'Not Bad'),
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
    )
    ranking = models.CharField(max_length=30, choices=ranking_choices)
    image = models.ImageField(upload_to='media/product', blank=True, null=True)

    def __str__(self):
        return self.name


# class Discount(models.Model):
#     discount_code = models.PositiveIntegerField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     amount = models.PositiveIntegerField()

#     def __str__(self):
#         return self.amount
