from django.db import models
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
    # name = models.CharField(_("name"), max_length=100)
    # title = models.CharField(_("Title"), max_length=100, help_text=_("The title of the book."))
    quantity = models.PositiveIntegerField(default=0)  # ???
    # description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug")
    data = models.JSONField(blank=True, null=True, default=dict)
    # data = models.JSONField(_("data"), blank=True, null=True, default=dict)
    # country = models.ManyToManyField("Country", related_name="country")
    country = models.ManyToManyField(Country, related_name="country")

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


# def upload_orig_path(instance, filename):
#     return f"images/{instance.product.brand}/orig/{filename}"
#
#
# def upload_lg_path(instance, filename):
#     return f"images/{instance.product.brand}/lg/{filename}"
#
#
# def upload_md_path(instance, filename):
#     return f"images/{instance.product.brand}/md/{filename}"
#
#
# def upload_sm_path(instance, filename):
#     return f"images/{instance.product.brand}/sm/{filename}"
#
#
# def upload_tn_path(instance, filename):
#     return f"images/{instance.product.brand}/tn/{filename}"


def upload_path(instance, filename):
    return f"images/Laced/{instance.product.category.get(type='B')}/{filename}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path)


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    sku = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField()  # ???
    # price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    variation = models.ManyToManyField("VariationOption", related_name="product_item")


class Price(models.Model):
    product = models.ForeignKey(
        "ProductItem", related_name="price", on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        # "Currency", on_delete=models.PROTECT, related_name="price"
        Currency,
        on_delete=models.PROTECT,
        related_name="price",
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.amount} {self.currency}"


class Variation(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.PROTECT)
    value = models.CharField(max_length=40, blank=True)
    data = models.JSONField(blank=True, default=dict)

    def __str__(self):
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
