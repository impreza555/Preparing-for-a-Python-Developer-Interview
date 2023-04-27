from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from products.forms import ProductForm
from products.models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView, FormView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    form_class = ProductForm
