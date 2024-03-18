from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent_category", "type")
    list_display_links = ("id", "name")
    list_filter = ("type",)
    fields = ["parent_category", "name", "description", "type"]
    ordering = ("id",)


class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ("get_img", "id", "product")
    # fields = ('title', 'movie', 'get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image.url } width="150">')

    get_img.short_description = mark_safe(f"<strong>Image</strong>")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # class ProductAdmin(TranslationAdmin):
    list_display = [
        "id",
        "name",
        "get_sku",
        "get_brand",
        "get_collections",
        "price",
        "is_active",
        # "data",
    ]

    filter_horizontal = ("category", "country")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "category",
                    "name",
                    "price",
                    "is_active",
                    "slug",
                    "data",
                    "country",
                ]
            },
        ),
    ]

    @admin.display(description="Brand")
    def get_brand(self, obj):
        return obj.category.get(type="B")

    @admin.display(description="Collections")
    def get_collections(self, obj):
        return [i for i in obj.category.filter(type="S")]

    @admin.display(description="SKU")
    def get_sku(self, obj):
        return obj.data["sku"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "get_img", "product")
    list_display_links = ("id", "get_img", "product")
    readonly_fields = ("get_img",)
    ordering = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": (("product"),),
            },
        ),
        (
            "Image",
            {
                "classes": ("wide", "extrapretty"),
                "fields": (
                    (
                        "get_img",
                        "image",
                    ),
                ),
            },
        ),
    )

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image.url } width="100">')

    get_img.short_description = mark_safe(f"<strong>Image</strong>")


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "sku", "quantity", "price")
    filter_horizontal = ("variation",)


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    filter_horizontal = ("products",)


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_display_links = ("id", "name")
    ordering = ("id",)


@admin.register(VariationOption)
class VariationOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "data", "variation", "get_brand")
    list_display_links = ("id", "value", "data")
    fieldsets = [(None, {"fields": ["variation", "value", "data"]})]
    ordering = ("id",)

    @admin.display(description="Type")
    def get_brand(self, obj):
        return obj.variation.category.name


@admin.register(AccountProduct)
class AccountProductAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(AvailableVariationOption)
class AvailableVariationOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "variation_option")
