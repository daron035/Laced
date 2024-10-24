from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.product.permissions import IsAdminOrReadOnly

from .models import Product
from .serializers import (
    GeneralProductSerializer,
    ProductSerializer,
)
from .session_views import get_session_currency


class SaleProductPagination(PageNumberPagination):
    page_size = 20
    # page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 4


from django.db.models import Q


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = SaleProductPagination
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super().get_queryset()
        print(f"Total objects before filter: {queryset.count()}")
        # queryset = queryset.filter(
        #     data__min_price_item__isnull=False, data__sizes__isnull=False
        # )
        queryset = queryset.filter(~Q(data__min_price_item=None))
        # Product.objects.filter(data__min_price_item__isnull=False, data__sizes__isnull=False)

        print(f"Total objects after filter: {queryset.count()}")
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductSerializer
        return GeneralProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        currency = get_session_currency(self.request)
        if currency is not None:
            context["preferences.currency__id"] = currency["id"]
            context["preferences.currency__symbol"] = currency["symbol"]
            context["preferences.currency__iso"] = currency["iso"]
        return context

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
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(product)
        data = serializer.data

        # Добавляем дополнительную информацию
        additional_info = {
            "additional_info": "Some additional info",
            # "currency": get_session_currency(request),
            "currency_id": self.get_serializer_context().get(
                "preferences.currency__id",
            ),
            "currency_symbol": self.get_serializer_context().get(
                "preferences.currency__symbol",
            ),
            "currency_iso": self.get_serializer_context().get(
                "preferences.currency__iso",
            ),
        }
        data.update(additional_info)

        return Response(data)

    @action(
        methods=["get"],
        detail=False,
        # url_path="er",
        # url_name="product-er",
        # permission_classes=[AllowAny],
    )
    def related_products(self, request):
        # queryset = self.get_queryset()[:20]
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=False,
    )
    def trending_now(self, request):
        queryset = self.get_queryset()[:3]
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
