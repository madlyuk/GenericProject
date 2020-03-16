from django.urls import path
from . import views


urlpatterns=[
    path("produttori",views.ManufacturerListView.as_view(),name="manufacturer_list"),
    path("produttori/<int:pk>/",views.ManufacturerDetailView.as_view(),name="manufacturer_detail"),
    path("prodotti",views.ProductListView.as_view(),name="product_list"),
    path("prodotti/<int:pk>",views.ProductDetailView.as_view(),name="product_detail")
]
