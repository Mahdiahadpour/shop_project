from django.urls import path, include
from .views import CustomerSignUp, AddressInput, ChangePasswordView, ProfileUpdateView
app_name = 'customers_api'
urlpatterns = [
    path('signup', CustomerSignUp.as_view(), name='signUp'),
    path('address', AddressInput.as_view(), name=' address_input'),
    path('changepassword', ChangePasswordView.as_view(), name='change_password'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
]
