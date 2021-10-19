from django.urls import path
from .views import product_add, c, product_history, product_detail, filter_products
from django.urls import path
# from orders.views import basket_view, delete_item_from_basket, checkout

app_name = 'product'

urlpatterns = [
    path('addproduct', product_add, name='productadd'),
    path('history', product_history),
    path('product_detials/<int:pk>', product_detail, name='product_detail'),
    path('categories/<str:category>', filter_products, name='categories'),
    path('product_history', product_history, name='product_history'),
    path('c', c)
]
