from django.forms import ModelForm, Select

from products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'measure_unit': Select(attrs={'class': 'browser-default'}),
        }
