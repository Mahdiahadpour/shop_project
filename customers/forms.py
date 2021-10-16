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


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())
    new_password_check = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ['password', 'new_password', 'new_password_check', ]
