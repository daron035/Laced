from django.utils.translation import get_language_from_request
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from app.product.models import (
    Product,
    Image,
    ProductItem,
    Price,
    Variation,
    VariationOption,
)
from app.purchases.models import Currency


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image")


class PriceSerializer(serializers.ModelSerializer):
    symbol = serializers.CharField(source="currency.symbol", read_only=True)
    currency = serializers.CharField(source="currency.iso", read_only=True)

    class Meta:
        model = Price
        fields = ("symbol", "currency", "value")


class GeneralProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    price_from = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "brand", "name", "image", "slug", "price_from")

    def get_brand(self, obj):
        return obj.category.get(type="B").name

    def get_price_from(self, obj):
        currency = self.context.get("preferences.currency__id")
        if currency:
            prices = Price.objects.filter(
                product=obj.data["min_price_item"], currency__id=currency
            ).first()
            return PriceSerializer(prices).data
        else:
            prices = Price.objects.filter(product=obj.data["min_price_item"])
        return PriceSerializer(prices, many=True).data
        # if not currency:
        #     prices = Price.objects.filter(
        #         product=obj.data["min_price_item"], currency__iso=1
        #     )
        # prices = Price.objects.filter(product=obj.data["min_price_item"])
        # def get_price_from(self, obj):
        #     # currency_cookie = self.context.get("request").COOKIES.get('currency')
        #     currency_cookie = self.context.get("request").COOKIES.get('currency')
        #     # self.session.get(settings.CART_SESSION_ID, None)
        #     request.session["currency"]
        #     request.session[""]

        # print(currency_cookie)
        if currency_cookie:
            price = Price.objects.get(
                product=obj.min_price_item, currency__iso=currency_cookie
            )
            if price:
                return PriceSerializer(price).data
        else:
            price = Price.objects.filter(product=obj.min_price_item)
            if price:
                return PriceSerializer(price, many=True).data
        return None

    def get_image(self, obj):
        request = self.context.get("request")
        image_instance = obj.image_set.first()
        if request and image_instance:
            return request.build_absolute_uri(image_instance.image.url)
        print("⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️⭕️")
        return None


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True, source="image_set.all")

    class Meta:
        model = Product
        fields = ("id", "name", "brand", "categories", "images")

    def get_brand(self, obj):
        return obj.category.get(type="B").name

    def get_categories(self, obj):
        return [category.name for category in obj.category.all()]

    def to_representation(self, obj):
        representation = super().to_representation(obj)

        representation["sku"] = obj.data.get("sku", None)
        representation["description"] = obj.data.get("description", None)
        representation["year_released"] = obj.data.get("year released", None)
        representation["colour"] = obj.data.get("colour", None)
        representation["sizes"] = obj.data.get("sizes", None)

        return representation


class CartProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    image = serializers.SerializerMethodField()
    # prices = serializers.SerializerMethodField()
    price_from = serializers.SerializerMethodField()
    variation = serializers.SerializerMethodField()

    class Meta:
        model = ProductItem
        fields = (
            "id",
            "name",
            "image",
            "variation",
            # "RUB",
            "prices",
            "price_from",
        )

    def get_price_from(self, obj):
        # currency = self.context.get("preferences.currency__id")
        context = self.context
        currency = context["preferences.currency__id"]
        if currency:
            # prices = Price.objects.filter(
            #     product=obj.data["min_price_item"], currency__id=currency
            # ).first()
            prices = Price.objects.get(
                product=obj.product.data["min_price_item"], currency__id=currency
            )
            return PriceSerializer(prices).data
        else:
            prices = Price.objects.filter(product=obj.product.data["min_price_item"])
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
