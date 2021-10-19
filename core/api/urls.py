from django.urls import path, include

urlpatterns = [
    path('v1/customers/', include('customers.api.urls', namespace='customers_api'))
]
