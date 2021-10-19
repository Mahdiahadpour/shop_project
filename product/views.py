from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from orders.models import Orders
from .forms import ProductAdd, CategoryAdd
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


# Create your views here.


def products(request):
    product = Product.objects.all()
    p = Paginator(product, 2)
    print(p.num_pages)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except (EmptyPage, PageNotAnInteger):
        page = p.page(1)
    return render(request, 'customers/index.html', {'product': page})


def filter_products(request, category):
    category_field = get_object_or_404(Category, category_name=category)
    product = Product.objects.filter(category=category_field)
    return render(request, 'customers/index.html', {'product': product})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


@login_required
def product_history(request):
    user = request.user
    last_items = Orders.objects.filter(customer=request.user).last()
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
        form = ProductAdd(request.POST, request.FILES)
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
