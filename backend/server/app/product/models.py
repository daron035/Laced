from django.db import models
from django.db.models import Min
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.postgres.indexes import GistIndex
from django.core.validators import MinValueValidator

from app.purchases.models import Account, Country, Currency


class AccountProduct(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"
        CANCELED = "CANCELED", "Canceled"

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_item = models.ForeignKey("ProductItem", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices)


class Category(models.Model):
    class ProductType(models.TextChoices):
        TYPE = "G", "General"
        BRAND = "B", "Brand"
        MODEL = "S", "Series"

    parent_category = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        choices=ProductType.choices, max_length=1, null=True, blank=True, default="B"
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(
        Category,
        blank=True,
        # on_delete=models.SET_NULL,
        # limit_choices_to={"type": ["S", "B"]},
        # limit_choices_to={"type": "B"},
    )
    name = models.CharField(max_length=100)
    # min_price_item = models.ForeignKey(
    #     "ProductItem",
    #     null=True,
    #     blank=True,
    #     on_delete=models.DO_NOTHING,
    #     # on_delete=models.SET_NULL,
    #     default=None,
    #     related_name="min_price_product",
    # )
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug")
    data = models.JSONField(blank=True, null=True, default=dict)

    @property
    def qty_in_stock(self):
        if self.productitem_set:
            return self.productitem_set.filter(
                product_id=self.pk, ordered_date=None
            ).count()

    # @property
    # def min_price(self):
    #     if self.productitem_set:
    #         return self.productitem_set.filter(product_id=self.pk).aggregate(Min('cat_id'))

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["slug", "name"]),
            # models.Index(fields=["first_name"], name="first_name_idx"),
            GistIndex(fields=["data"]),
            # GistIndex(fields=['data'], name='json_field_gist_index')
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    # @property
    # def image(self):
    #     images = self.images.all()
    #     if images.count() == 0:
    #         return None
    #     return images.first()


def upload_path(instance, filename):
    return f"images/Laced/{instance.product.category.get(type='B')}/{filename}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path)


###############################################
class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
    sku = models.CharField(max_length=40, blank=True)
    variation = models.ManyToManyField(
        "VariationOption", related_name="product_item", blank=False
    )
    date_added = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True, blank=True)
    prices = models.ManyToManyField(Currency, through="Price")

    def __str__(self):
        return f"{self.id} {self.product.name} (id {self.product.id})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Check if any two VariationOption instances have the same variation_id
        variation_ids = set()
        for variation_option in self.variation.all():
            if variation_option.variation_id in variation_ids:
                # Rollback the transaction
                self.delete()
                raise ValueError(
                    "Two VariationOptions with the same variation_id are not allowed."
                )
            variation_ids.add(variation_option.variation_id)


###############################################



# 🚨 product
class Price(models.Model):
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    value = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.currency.symbol} {self.value}"
    
    class Meta:
        ordering = ['currency']


# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=ProductItem)
# def create_price(sender, instance, created, *args, **kwargs):
#     if created:
#         # r = kwargs.get('rub')
#         # r =kwargs.pop('RUB', None)
#         r = args[0]
#         Price.objects.create(product=instance, RUB=r)
class Variation(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.PROTECT)
    value = models.CharField(max_length=40, null=True, blank=True)
    data = models.JSONField(blank=True, default=dict)

    def __str__(self):
        if self.value is None:
            dict_as_string = " | ".join(
                [f"{key} {value}" for key, value in self.data.items()]
            )
            return dict_as_string
        return str(self.value)


class AvailableVariationOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    variation_option = models.ForeignKey(VariationOption, on_delete=models.PROTECT)


# class Country(models.Model):
#     COUNTRY_CHOICES = [
#         ("RU", "Russian Federation"),
#         ("KZ", "Kazakhstan"),
#         ("BY", "Belarus"),
#     ]
#     name = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default="RU")
#
#     def __str__(self):
#         return self.get_name_display()  # name
#
#     class Meta:
#         verbose_name_plural = "Countries"
#
#
# class Currency(models.Model):
#     CURRENCY_CHOICES = [
#         ("USD", "US Dollar"),
#         ("EUR", "Euro"),
#         ("RUB", "Russian Ruble"),
#         ("KZT", "Kazakhstani Tenge"),
#         ("BYN", "Belarusian Ruble"),
#     ]
#     value = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="RUB")
#
#     def __str__(self):
#         return self.value


class Carousel(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name="carousel")


# @receiver(m2m_changed, sender=ProductItem.variation.through)
# def check_option_variation(sender, instance, action, pk_set, **kwargs):
#     if action == 'validate_variations':
#         new_variations = VariationOption.objects.filter(pk__in=pk_set).values_list('variation_id', flat=True)
#         if len(set(new_variations)) != len(new_variations):
#             raise ValidationError("Duplicate variation detected in Options.")
#     elif action == 'pre_add':
#         existing_variations = instance.variation.values_list('variation_id', flat=True)
#         new_variations = VariationOption.objects.filter(pk__in=pk_set).values_list('variation_id', flat=True)
#         if set(existing_variations) & set(new_variations):
#             raise ValidationError("Duplicate variation detected in Options.")
