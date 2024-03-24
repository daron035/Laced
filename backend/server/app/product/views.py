from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework import status
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
    # page_size = 20
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 4


# class ProductViewSet(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.ListModelMixin,
#     GenericViewSet,
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#     pagination_class = SaleProductPagination
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         page = self.paginate_queryset(queryset)
#         serializer = self.get_serializer(queryset, many=True)
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = self.get_queryset()
#         product = queryset.filter(slug=pk).first()
#         if product:
#             serializer = self.get_serializer(product)
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     # def get_queryset(self):  # переопределяем queryset
#     #     pk = self.kwargs.get("pk", None)
#     #     style_codes = self.request.query_params.get("style_codes", None)
#     #     # print(self.request.locale)
#     #     if pk:
#     #         print("pk", pk)
#     #         return Product.objects.filter(slug=pk)
#     #     else:
#     #         query_set = Product.objects.all()
#     #         if style_codes is None:
#     #             return Product.objects.all()[:20]
#     #         return query_set.filter(data__sku__in=style_codes.split(","))
#
#     # def list(self, request):
#     # def retrieve(self, request, pk=None):
#     #     queryset = Product.objects.all()
#     #     user = get_object_or_404(queryset, pk=pk)
#     #     serializer = UserSerializer(user)
#     #     return Response(serializer.data)
#
#     # def list(self, request):
#     #     queryset = self.get_queryset()
#     #     serializer = self.get_serializer(queryset, many=True)
#     #     return Response(serializer.data)
#     #
#     # def retrieve(self, request, pk=None):
#     #     queryset = self.get_queryset()
#     #     product = queryset.filter(slug=pk).first()
#     #     if product:
#     #         serializer = self.get_serializer(product)
#     #         return Response(serializer.data)
#     #     else:
#     #         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     # def list(self, request, *args, **kwargs):
#     #     # headers = request.META
#     #     # pprint(headers)
#     #
#     #     # print("000000", request.COOKIES.get("asdf", None), "\n")
#     #     # print("000000", request.COOKIES.get("refresh"))
#     #     # accept_language = request.headers.get("Accept-Language", "")
#     #     # print("Accept-Language:", accept_language)
#     #     print()
#     #     print("23981092943189284902")
#     #     print()
#     #
#     #     return super().list(request, *args, **kwargs)


class ProductViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = SaleProductPagination
    lookup_field = "slug"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            product = self.get_queryset().get(slug=self.kwargs.get("slug"))
        except Product.DoesNotExist:
            # raise NotFound("Product not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(product)
        return Response(serializer.data)
