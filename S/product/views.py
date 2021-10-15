from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Product
from .forms import ProductAdd, CategoryAdd


# Create your views here.

def products(request):
    product = Product.objects.all()
    return render(request, 'customers/index.html', {'product': product})



def product_add(request):
    print(request.method)
    if request.method == 'POST':
        form = ProductAdd(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('Ok!')
    else:
        form = ProductAdd()
        return render(request, 'product/productadd.html', {'form': form})


def c(request):
    if request.method == 'POST':
        form = CategoryAdd(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('Ok!')
    else:
        form = CategoryAdd()
        return render(request, 'product/C.html', {'form': form})

# def Discount(request):
# pro
