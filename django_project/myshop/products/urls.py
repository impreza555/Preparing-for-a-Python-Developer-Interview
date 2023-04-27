from django.urls import path

from products.views import ProductListView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('add/', ProductCreateView.as_view(), name='add'),
]
