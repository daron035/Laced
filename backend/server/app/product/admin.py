from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django.db.models import Min, F, Count, Q, Prefetch, Sum


from .models import *
# from .signals import validate_option_variation, validate_variations
from .signals import validate_variations, validate_prices, update_product_entry


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
    list_display = [
        "id",
        "name",
        "get_img",
        "get_sku",
        "get_brand",
        "get_collections",
        "is_active",
        "get_qty_in_stock",
        "get_min_price_item",
        # "data",
    ]

    filter_horizontal = ("category",)
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
                    "is_active",
                    "slug",
                    "data",
                ]
            },
        ),
    ]

    @admin.display(description="Min price")
    def get_min_price_item(self, obj):
        if obj.min_price_item:
            prices = Price.objects.filter(product=obj.min_price_item)
            ids = [obj.min_price_item.pk] + [price for price in prices]
            return mark_safe("id " + "<br>".join(map(str, ids)))
        else:
            return None
    
    @admin.display(description="In Stock")
    def get_qty_in_stock(self, obj):
        return obj.qty_in_stock

    @admin.display(description="IMG")
    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image_set.first().image.url } width="80">')
    # get_img.short_description = mark_safe(f"<strong>IMG</strong>")

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




class PriceInlineFormset(forms.models.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        currencies = Currency.objects.all()[:3]
        for i, form in enumerate(self.forms):
            form.initial['currency'] = currencies[i % len(currencies)].pk
            # form.initial['currency'] = currencies[i % 4].pk
        # for form, currency in zip(self.forms, currencies[:4]):
        #     form.initial['currency'] = currency.pk


class PriceInline(admin.TabularInline):
    model = Price
    formset = PriceInlineFormset

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # Отключаем выбор валюты (currency) в виджете
        formset.form.base_fields['currency'].disabled = True
        if obj:
            formset.extra = 0  # Для редактирования существующего объекта
        else:
            formset.extra = 3  # Для добавления нового объекта
        return formset
    


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product","get_variation","get_prices",)
    # list_display = ("id", "product","get_variation")
    # list_display = ("id", "product", "get_variation", "get_prices")
    ordering = ("id",)
    # readonly_fields = ("get_qty_in_stock",)
    # readonly_fields = ("get_qty_in_stock",)
    list_display_links = ("id", "product")
    # filter_horizontal = ("variation",)
    inlines = [PriceInline]
    # fieldsets = (
    #     (None, {
    #         'fields': ('get_qty_in_stock',),  # Добавление поля в fieldsets
    #     }),
    # )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("product").prefetch_related("variation")

    @admin.display(description="Prices")
    def get_prices(self, obj):
        prices = Price.objects.filter(product=obj)
        if prices.exists():
            return " ".join([str(price) for price in prices])
        return None
    
    # @admin.display(description="Quantity in stock")
    # def get_qty_in_stock(self, obj):
    #     return obj.qty_in_stock  # Вызов метода get_qty_in_stock
    # get_qty_in_stock.short_description = 'Quantity in stock'
    
    def get_variation(self, obj):
        return ", ".join([f"{var.id} | {var}" for var in obj.variation.all()])
    get_variation.short_description = "Size"

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        instance = form.instance
        validate_variations(pk_set=instance.variation.all())
        validate_prices(pk_set=instance.price_set.all())
        # validate_prices(pk_set=Price.objects.filter(product=instance))
        update_product_entry(instance=instance)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "currency", "value")
    list_display_links = ("id", "product")

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
