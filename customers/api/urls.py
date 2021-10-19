from django.urls import path, include
from .views import CustomerSignUp, AddressInput, ChangePasswordView, ProfileUpdateView

urlpatterns = [
    path('signup', CustomerSignUp.as_view(), name='signUp'),
    path('address', AddressInput.as_view(), name=' adressinput'),
    path('changepassword', ChangePasswordView.as_view(), name='changepassword'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'),
         name='password_reset'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
]
