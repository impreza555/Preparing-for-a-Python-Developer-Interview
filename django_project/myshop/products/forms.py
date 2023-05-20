from django.forms import ModelForm, Select

from products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'date':
                field.widget.attrs['class'] = 'datepicker'
            else:
                field.widget.attrs['class'] = 'input-field col s12'
