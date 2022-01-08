import kwargs as kwargs
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import NoteBook, Category
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'main/index.html')


class Home(ListView):
    queryset = NoteBook.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class Detail(DetailView):
    queryset = NoteBook.objects.all()
    template_name = 'main/Detail.html'
    context_object_name = 'products'

    cart_product_form = CartAddProductForm
    extra_context = {'cart_product_form': cart_product_form}

    pk_url_kwarg = 'pk'


class CategoryView(ListView):
    template_name = 'main/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = NoteBook.objects.filter(category_id=self.kwargs.get('category_id'))
        return queryset
