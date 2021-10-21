from django.urls import path, include

urlpatterns = [
    path('v1/customers/', include('customers.api.urls', namespace='customers_api')),
    path('v1/orders/',include('orders.api.urls', namespace='orders_api'))
]
