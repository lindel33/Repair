from django.shortcuts import render
from django.views.generic import TemplateView


class Cart(TemplateView):
    template_name = 'main/cart.html'
