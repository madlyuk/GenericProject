from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Manufacturer, Product

# Create your views here.
class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "products/manufacturer_list.html"
class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "products/manufacturer_detail.html"
class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
