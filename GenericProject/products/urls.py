from django.urls import path
from . import views


urlpatterns=[
    path("produttori",views.ManufacturerListView.as_view(),name="manufacturer_list"),
    path("produttori/<int:pk>/",views.ManufacturerDetailView.as_view(),name="manufacturer_detail"),
    path("prodotti",views.ProductListView.as_view(),name="product_list"),
    path("prodotti/<int:pk>",views.ProductDetailView.as_view(),name="product_detail")
]

#API_v1 (JsonResponse)
urlpatterns+=[
    path("api_v1/manufacturers",views.manufacturer_list_view,name="manufacturer_list_api_v1"),
    path("api_v1/manufacturers/<int:pk>/",views.manufacturer_detail_view,name="manufacturer_detail_api_v1"),
    path("api_v1/products",views.product_list_view,name="product_list_api_v1"),
    path("api_v1/products/<int:pk>",views.product_detail_view,name="product_detail_api_v1")
]