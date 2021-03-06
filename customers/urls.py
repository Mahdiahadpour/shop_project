from django.urls import path
from .views import my_login, user_profile, my_logout, edit_profile, change_password_view
from product.views import products, filter_products

app_name = 'customers'
urlpatterns = [
    path('login/', my_login, name='login'),
    path('', products, name='index'),
    path('filter_category/<str:category>', filter_products, name='index'),
    path('profile/', user_profile, name='profile'),
    path('logout/', my_logout, name='log out'),
    path('edit-profile/', edit_profile, name='edit profile'),
    path('change_password/', change_password_view, name='change_password')
]
