from django.contrib import admin
from orders.models import Discount, Payment, OrderItem, Orders, Shipment


class Orders_Register(admin.ModelAdmin):
    list_display = [
        "customer",
        "deleted",
        "fulfilled_time",
        "shipment_method",
        "total",
    ]


admin.site.register(Discount)
admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Orders, Orders_Register)
admin.site.register(Shipment)
# Register your models here.
