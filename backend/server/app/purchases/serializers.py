from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from app.product.models import (
    Price,
    ProductItem,
)
from app.product.serializers import PriceSerializer


class PaymentSerializer(serializers.Serializer):
    token = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class CartProductSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(source="product.id")
    name = serializers.CharField(source="product.name")
    image = serializers.SerializerMethodField()
    # prices = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    variation = serializers.SerializerMethodField()

    class Meta:
        model = ProductItem
        fields = (
            "id",
            "product_id",
            "name",
            "image",
            "variation",
            # "RUB",
            # "prices",
            "price",
        )

    def get_price(self, obj):
        currency = self.context.get("preferences.currency__id")
        if currency:
            prices = Price.objects.filter(
                # product=obj.data["min_price_item"], currency__id=currency
                product=obj,
                currency__id=currency,
            ).first()
            return PriceSerializer(prices).data
        else:
            prices = Price.objects.filter(product=obj.data["min_price_item"])
        return PriceSerializer(prices, many=True).data

    def get_image(self, obj):
        request = self.context.get("request")
        image_instance = obj.product.image_set.first()
        if request and image_instance:
            return request.build_absolute_uri(image_instance.image.url)
        return None

    # def get_prices(self, obj):
    #     return PriceSerializer(obj.price).data

    def get_variation(self, obj):
        try:
            # size_var = Variation.objects.get(name__iexact="size")
            # return str(obj.variation.get(variation=size_var))
            return str(obj.variation.get(variation=1))
        except ObjectDoesNotExist:
            return None

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation["variation_id"] = obj.variation.get(variation=1).id
        return representation
