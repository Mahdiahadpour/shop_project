from django.urls import path
from .views import add_item_view, basket

app_name = 'orders'
urlpatterns = [
    path('basket/', basket, name='basket'),
    # path('basket/delete/', delete_item_from_basket, name='delete_item_from_basket'),
    # path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:pk>', add_item_view, name='add_to_cart')
]
