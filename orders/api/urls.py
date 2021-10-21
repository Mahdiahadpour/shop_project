from django.urls import path
from .views import DiscountView

app_name = 'orders_api'
urlpatterns = [
    path('discount', DiscountView.as_view(), name='discount')
]