from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import NoteBook
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'main/index.html')


class Home(ListView):
    queryset = NoteBook.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'products'


class Detail(DetailView):
    queryset = NoteBook.objects.all()
    template_name = 'main/Detail.html'
    context_object_name = 'products'

    cart_product_form = CartAddProductForm
    extra_context = {'cart_product_form': cart_product_form}

    pk_url_kwarg = 'pk'
