from django.urls import path
from .views import product_add, c
from django.urls import path
from orders.views import basket_view, delete_item_from_basket, checkout

app_name = 'product'

urlpatterns = [
    path('addproduct', product_add, name='productadd'),
    path('c', c, name='c'),

]
