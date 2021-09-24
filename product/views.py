from django.shortcuts import render
from .models import Category, Product


# Create your views here.

def products(request):
    product = Product.objects.all()
    return render(request, 'customers/index.html', {'product': product})
