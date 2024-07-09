from django.shortcuts import render
from django import http
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import Order, OrderItem
from orders.tasks import order_created


User = get_user_model()


def create_order(request: http.HttpRequest):
    user = User.objects.get(id=request.user.id)
    cart = Cart(request)
    order_form = OrderCreateForm(
        data=request.POST or None,
        initial=model_to_dict(user)
    )

    if request.method == 'POST' and order_form.is_valid():
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

        order_created.delay(order.id)
        cart.clear()
        return render(request, 'orders/order_created.html', {'order': order})

    return render(
        request,
        'orders/order_create.html',
        {'order_form': order_form}
    )
