from django.urls import path, include
from .views import CustomerSignUp, AddressInput, ChangePasswordView, ProfileUpdateView
# from django_rest_passwordreset .urls import
app_name = 'customers_api'
urlpatterns = [
    path('signup', CustomerSignUp.as_view(), name='signUp'),
    path('address', AddressInput.as_view(), name=' adressinput'),
    path('changepassword', ChangePasswordView.as_view(), name='changepassword'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
]
