from django.urls import path
from .views import my_login, user_profile, my_logout, edit_profile
from product.views import products

urlpatterns = [
    path('login/', my_login, name='login'),
    path('', products, name='index'),
    path('profile/', user_profile, name='profile'),
    path('logout/', my_logout, name='log out'),
    path('edit-profile', edit_profile, name='edit profile')
]
