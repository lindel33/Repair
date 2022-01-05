from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import NoteBook


def index(request):
    return render(request, 'main/index.html')


class Home(TemplateView):
    template_name = 'main/index.html'


class Detail(DetailView):
    queryset = NoteBook.objects.all()
    template_name = 'main/Detail.html'
    context_object_name = 'products'
    pk_url_kwarg = 'pk'
