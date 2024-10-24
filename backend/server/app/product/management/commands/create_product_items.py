from random import choice, uniform, sample, randint
import random

from django.db.models import F
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from app.product.models import Product, ProductItem, VariationOption, Price
from app.purchases.models import Currency
from app.product.signals import my_signal, update_product_entry


class Command(BaseCommand):
    help = "Creates a superuser account"

    def handle(self, *args, **options):

        if ProductItem.objects.all().exists():
            ProductItem.objects.all().delete()

        for product in Product.objects.all():
            product.data["sizes"] = None
            product.data["min_price_item"] = None
            product.save()

        currencies = Currency.objects.filter(pk__in=[1, 3, 4])
        var_opts = VariationOption.objects.all()[101:]
        ls = [97,162,169,183,194,202,213,228,242,100]

        for i in range(10000):
            random_product = Product.objects.get(pk=choice(ls))
            # random_product = Product.objects.get(pk=random.randint(1, 100))

            product_item = ProductItem.objects.create(product=random_product)
            # product_item.save()

            product_item.variation.set([choice(var_opts)])

            for currency in currencies:
                price = Price(
                    product=product_item,
                    currency=currency,
                    value=round(uniform(100.00, 10000.00), 2),
                )
                price.save()

            product_item.save()
            # update_product_entry(product_item)
            my_signal.send(
                sender=None,
                instance=product_item,
                variation_pk_set=product_item.variation.all(),
                prices=product_item.price_set.all(),
            )
