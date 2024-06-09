from django.shortcuts import render
from django import http
from django.contrib.auth import get_user_model

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import Order, OrderItem


User = get_user_model()


def create_order(request: http.HttpRequest):
    cart = Cart(request)
    order_form = OrderCreateForm(request.POST or None)

    if request.method == 'POST' and order_form.is_valid():
        user = User.objects.get(id=request.user.id)
        order: Order = order_form.save(commit=False)
        order.first_name = user.first_name
        order.last_name = user.last_name
        order.email = user.email
        order.save()

        for item in cart:
            OrderItem.objects.create(
                product=item['product'],
                order=order,
                price=item['price'],
                quantity=item['quantity'],
            )

        cart.clear()
        return render(request, 'orders/order_created.html', {'order': order})

    return render(
        request,
        'orders/order_create.html',
        {'order_form': order_form}
    )
