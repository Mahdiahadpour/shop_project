from django import forms
from .models import Orders
class BasketForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['costumer_massage','address']