from django.contrib import admin

from products.models import Product, Suppliers

admin.site.register(Product)
admin.site.register(Suppliers)
