from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    context_object_name = 'all_products'
    queryset = Product.objects.all()
    template_name = 'products/products.html'