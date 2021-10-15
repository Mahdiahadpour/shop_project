from django import forms
from .models import Product, Category


class ProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryAdd(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'