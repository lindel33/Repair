from django.views.generic import TemplateView


from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from repair_home.models import NoteBook

from .cart import Cart

from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(NoteBook, id=product_id)
    form = CartAddProductForm(request.POST)

    with open('log.txt', 'a') as f:
        # f.write('Перед is_valid')
        f.write(str(form))
        # f.write(str(product))
        # f.write(str(cart))


    if form.is_valid():
        with open('log.txt', 'a') as f:
            f.write('После is_valid')
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect('/cart')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(NoteBook, id=product_id)
    cart.remove(product)
    return redirect('/cart')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'main/cart.html', {'cart': cart})



