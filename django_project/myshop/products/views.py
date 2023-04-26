from django.shortcuts import render
from django.views.generic import ListView, FormView

from products.forms import ProductForm
from products.models import Product


class ProductModelListView(ListView, FormView):
    form_class = ProductForm
    template_name = 'index.html'
    queryset = Product.objects.all()
