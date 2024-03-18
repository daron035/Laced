from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from pprint import pprint

from app.product.permissions import IsAdminOrReadOnly

from .models import Product
from .serializers import ProductSerializer


class SaleProductPagination(PageNumberPagination):
    page_size = 20
    # page_size = 3
    page_size_query_param = "page_size"
    # max_page_size = 3


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = SaleProductPagination

    def get_queryset(self):  # переопределяем queryset
        pk = self.kwargs.get("pk", None)
        style_codes = self.request.query_params.get("style_codes", None)
        print(self.request.locale)
        if pk:
            print("pk", pk)
            return Product.objects.filter(data__sku__in=pk.split(","))
        else:
            query_set = Product.objects.all()
            if style_codes is None:
                return Product.objects.all()[:20]
            return query_set.filter(data__sku__in=style_codes.split(","))

    # def list(self, request, *args, **kwargs):
    #     # headers = request.META
    #     # pprint(headers)
    #
    #     # print("000000", request.COOKIES.get("asdf", None), "\n")
    #     # print("000000", request.COOKIES.get("refresh"))
    #     # accept_language = request.headers.get("Accept-Language", "")
    #     # print("Accept-Language:", accept_language)
    #     print()
    #     print("23981092943189284902")
    #     print()
    #
    #     return super().list(request, *args, **kwargs)
