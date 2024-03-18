from django.utils.translation import get_language_from_request
from rest_framework import serializers

from app.product.models import Product, Image


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "image")

    def get_image(self, obj):
        request = self.context.get("request")
        image_instance = obj.image_set.first()
        if request and image_instance:
            return request.build_absolute_uri(image_instance.image.url)
        return None

    def to_representation(self, obj):
        representation = super().to_representation(obj)

        representation["sku"] = obj.data.get("sku", None)
        representation["year_released"] = obj.data.get("year released", None)

        return representation
