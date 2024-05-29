from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import HttpRequest
from django.contrib import messages

from cart.cart import Cart
from cart.forms import CartAddProductForm
from catalog.models import Product


@require_POST
def cart_add_product(request: HttpRequest, product_id: int):
    cart = Cart(request)
    cart_form = CartAddProductForm(request.POST)
    product = get_object_or_404(Product, id=product_id)

    if cart_form.is_valid():
        cd = cart_form.cleaned_data
        cart.add(product, cd['quantity'], cd['override'])

        if cd['override']:
            messages.success(
                request,
                'Количество товара было успешно изменено!'
            )
            return redirect('cart:cart_detail')

        messages.success(request, 'Товар успешно добавлен в корзину!')

    return redirect(product.get_absolute_url())


@require_POST
def cart_remove_product(request: HttpRequest, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    messages.success(request, 'Товар успешно удален из корзины!')

    return redirect('cart:cart_detail')


def cart_detail(request: HttpRequest):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'override': True,
            }
        )
    return render(request, 'cart/cart_detail.html', {'cart': cart})
