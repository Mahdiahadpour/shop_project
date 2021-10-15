from django.urls import path
from .views import CustomerSignUp, AddressInput

urlpatterns = [
    path('signup', CustomerSignUp.as_view(), name='signUp'),
    path('address', AddressInput.as_view(), name=' adressinput')
]
