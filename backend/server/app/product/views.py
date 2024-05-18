from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from app.product.permissions import IsAdminOrReadOnly

from .models import Product
from .serializers import ProductSerializer, GeneralProductSerializer
from .session_views import session_currency


class SaleProductPagination(PageNumberPagination):
    # page_size = 20
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 4


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = SaleProductPagination
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(data__min_price_item__isnull=False, is_active=True)
        # return queryset.filter(min_price_item__isnull=False, is_active=True)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductSerializer
        return GeneralProductSerializer

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

    @action(
        methods=["get"],
        detail=False,
        # url_path="er",
        # url_name="product-er",
        # permission_classes=[AllowAny],
    )
    def related_products(self, request):
        queryset = self.get_queryset()[:3]
        currency_id = session_currency(request)
        context = {}
        if currency_id is not None:
            context["preferences.currency__id"] = currency_id
        serializer = self.get_serializer(
            queryset,
            many=True,
            context=context,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=False,
    )
    def trending_now(self, request):
        queryset = self.get_queryset()[:3]
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
