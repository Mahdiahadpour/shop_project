from django.contrib import admin
from .models import Product, Category

# Register your models here.
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Discount)