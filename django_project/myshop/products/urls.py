from django.urls import path

from products.views import ProductModelListView

urlpatterns = [
    path('', ProductModelListView.as_view(), name='index'),
]
