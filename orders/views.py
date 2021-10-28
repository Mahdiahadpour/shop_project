from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from orders.models import Discount, Orders
from product.models import Product
from .models import OrderItem
from .forms import BasketForm


# Create your views here.
@login_required()
def add_item_view(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = OrderItem.objects.create(product=item)
    order_qs = Orders.objects.filter(customer=request.user)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_detail.filter(product_id=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
    else:

        order = Orders.objects.create(customer=request.user, id=pk)
        order.order_detail.add(order_item)
    return redirect('product:product_detail', pk=pk)


def basket(request):
    order = Orders.objects.filter(customer=request.user)
    return render(request, 'orders/basket.html', {'order': order})


def basket_form(request):
    form = BasketForm()

    if form.is_valid():
        form.save()
        return redirect('orders:basket')
    return render(request, 'orders/basket.html', {'form': form})
