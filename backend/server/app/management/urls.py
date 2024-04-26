from django.urls import path
from .views import *


urlpatterns = [
    path("", ProductView.as_view()),
    path("add-product/", AddProductView.as_view(), name="add_product"),
    # path("add-product/load_options/", load_options, name="load_options"),
    path("add-product/load_brands/", load_brands, name="load_brands"),
    path("add-product/load_series/", load_series, name="load_series"),
    path("search-product/", search_product, name="search_product"),
    path("index2/", index2, name="ab"),
]
