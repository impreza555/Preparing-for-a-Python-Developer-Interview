from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from products.forms import ProductForm
from products.models import Product


class ProductListView(ListView, FormView):
    form_class = ProductForm
    template_name = 'index.html'
    queryset = Product.objects.select_related('supplier').all()


class ProductCreateView(CreateView, FormView):
    template_name = 'modal.html'
    success_url = reverse_lazy('index')
    form_class = ProductForm
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.method == "GET" and self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = {
                'form_is_valid': False,
                'html_form': response.rendered_content
            }
            return JsonResponse(data)
        else:
            return response
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.method == "POST" and self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = {
                'form_is_valid': True,
                'html_good_list': render_to_string(
                    'inc/table.html', {
                        'object_list': Product.objects.select_related('supplier').all()
                    }),
            }
            return JsonResponse(data)
        else:
            return response
