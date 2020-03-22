from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Manufacturer, Product

# Create your views here.

#Viste destinate alle API v.1 usando i tool standard di Django, ovvero http.JsonResponse

def product_list_view(request):
    products = Product.objects.all()
    data = {"products":list(products.values("pk","name","manufacturer__name","description","photo","price","shipping_cost","quantity"))}
    response = JsonResponse(data)
    return response

def product_detail_view(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        data={
            "product":{
                "name":product.name,
                "manufacturer":product.manufacturer.name,
                "description":product.description,
                "photo":product.photo.url,
                "price":product.price,
                "shipping_cost":product.shipping_cost,
                "quantity":product.quantity
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
       response = JsonResponse({
               "error":{
                        "code": 404,
                        "message": "Prodotto non trovato"
                        }},
                status=404
       )
    return response

def manufacturer_list_view(request):
    manufacturers = Manufacturer.objects.all()
    data = {"manufacturers":list(manufacturers.values("pk","name","location","active"))}
    response = JsonResponse(data)
    return response

def manufacturer_detail_view(request,pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data={
            "manufacturer":{
                "pk":manufacturer.pk,
                "name":manufacturer.name,
                "location":manufacturer.location,
                "active":manufacturer.active,
                "products":list(manufacturer.products.values("pk","name","manufacturer__name","description","photo","price","shipping_cost","quantity"))
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
       response = JsonResponse({
               "error":{
                        "code": 404,
                        "message": "Produttore non trovato"
                        }},
                status=404
       )
    return response


#Viste destinate alle API v.2 usando Django REST API


#Viste destinate al CATALOGO
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
