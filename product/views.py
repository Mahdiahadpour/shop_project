from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from orders.models import Orders
from .forms import ProductAdd, CategoryAdd


# Create your views here.


def products(request):
    product = Product.objects.all()
    return render(request, 'customers/index.html', {'product': product})


def filter_products(request, category):
    category_feild = get_object_or_404(Category, category_name=category)
    product = Product.objects.filter(category=category_feild)
    return render(request, 'customers/index.html', {'product': product})


def product_detial(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template_name = 'product/product_detial.html'
    context = {'product': product}
    return render(request, template_name, context)


@login_required
def product_history(request):
    user = request.user
    last_items = Orders.objects.filter(customer=user).last()
    list_item = []
    if last_items:
        for item in last_items.order_detail.all().order_by('-pk')[:10]:
            print(item.quantity)
            print(item.product)
            list_item.append(item)
            # list_item.append(item.order_detial.product)

    else:
        return HttpResponse("You don't have orders yet!")

    template_name = 'product/history_order.html'
    context = {'items': list_item}
    return render(request, template_name, context)


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
