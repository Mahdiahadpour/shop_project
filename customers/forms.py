from django import forms

from .models import Customer


class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']


class UserProfile(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'birthday', 'mobile_number', 'home_number', 'image']
