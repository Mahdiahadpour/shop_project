from django.urls import path
from .views import productadd, c, products

urlpatterns = [
    path('addproduct', productadd, name='productadd'),
    path('c', c, name='c'),
    path('d/', products, )
]
