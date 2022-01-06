from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import NoteBook


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

    pk_url_kwarg = 'pk'
