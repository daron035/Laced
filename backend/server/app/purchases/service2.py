from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from django.db.models import Count, Q
from django.db.models import Sum, Min
import ipinfo
from enum import Enum

from app.product.serializers import ProductSerializer
from app.product.models import Price, Product, ProductItem
from app.product.session_views import get_session_currency

from .serializers import CartProductSerializer


class Currency(Enum):
    US = "USD"
    UK = "GBP"
    EU = "EUR"
    RU = "RUB"
    KZ = "KZT"
    BY = "BYN"


class Preferences:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        preferences = self.session.get("preferences", None)
        if preferences is None:
            # save an empty preferences in session
            preferences = self.session["preferences"] = {}
        self.preferences = preferences
        if "preferred_country" and "preferred_currency" not in self.preferences:
            if request.user.is_authenticated:
                country = request.user.account.country.iso
                currency = request.user.account.currency.iso
            else:
                # country = get_ip_details("168.156.54.5").country
                country = "US"
                print("ASDIOFJIQWEJFPIOEQRJFIOJREIFJ389J8394JFASDJFKLSDJFKLASJDF")
                currency = Currency[country].value
            self.preferences["preferred_country"] = country
            self.preferences["preferred_currency"] = currency
            print(self.preferences)
            self.save()
            # request.session.modified = True

    def save(self):
        self.session.modified = True

    def verify(self):
        cookies_list = ["preferred_currency", "preferred_country"]
        for i in cookies_list:
            if i in self.account:
                pass

    def save(self):
        self.session.modified = True


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if cart is None:
            # save an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def get_serializer_context(self):
        """
        Добавление метода get_serializer_context для передачи контекста в сериализатор.
        """
        context = {
            "request": self.request,
            "view": self,
        }
        currency = get_session_currency(self.request)
        if currency:
            context["preferences.currency__id"] = currency["id"]
            context["preferences.currency__iso"] = currency["iso"]
        return context

    def save(self):
        self.session.modified = True

    def add(self, product_id, variation_id, quantity, overide_quantity=False):
        # {'2': {'variation_id': 108, 'quantity': 5}, '3': {'quantity': 5, 'price': '1800.00'}}
        """
        Add product to the cart or update its quantity
        """
        product_item_id = str(product_id)
        if product_item_id in self.cart:
            raise ValueError("Product already exists in the cart.")
        if product_item_id not in self.cart:

            matching_product_items = ProductItem.objects.annotate(
                variation_count=Count("variation")
            ).filter(
                product_id=product_id, variation__id=variation_id, variation_count=1
            )
            aggregated = (
                Price.objects.filter(product__in=matching_product_items)
                .values("product_id", "product__date_added")
                .annotate(total_value=Sum("value"))
                .order_by("total_value", "product__date_added")
            )
            min_total_value = aggregated.aggregate(min_value=Min("total_value"))[
                "min_value"
            ]
            min_price_product_id = aggregated.filter(
                total_value=min_total_value
            ).first()
            # print()
            # print('matching_product_items',matching_product_items)
            # print()
            # print('aggregated', aggregated)
            # print()
            # print('min_total_value', min_total_value)
            # print()
            # print('min_price_product_id',min_price_product_id)
            # print()
            # return
            # self.cart[product_item_id] = {
            #     "product_id": min_price_product_id,
            #     "quantity": 0,
            # }
            product_item_id = min_price_product_id
            self.cart[product_item_id] = 0
        if overide_quantity:
            self.cart[product_item_id] = quantity
        else:
            self.cart[product_item_id] += quantity
        self.save()
        print(self.cart)

    def remove(self, product_item_id):
        """
        Remove a product from the cart
        """
        product_id = str(product_item_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def data(self):
        return self.cart

    def __iter__(self):
        """
        Loop through cart items and fetch the products from the database
        """
        # {'2': {'variation_id': 108, 'quantity': 5}, '3': {'quantity': 5, 'price': '1800.00'}}
        # return self.cart
        context = self.get_serializer_context()
        product_ids = self.cart.keys()
        products = ProductItem.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            # {'quantity': 5, 'price': '1800.00'}
            # print(cart[str(product.id)])

            serializer = CartProductSerializer(
                # product, context={"request": self.request}
                product,
                context=context,
            )
            # print(serializer.data)
            # cart[str(product.pk)]["product"] = serializer.data
            cart[str(product.pk)] = serializer.data
            # print("1", cart[str(product.id)]["product"], "\n")
            # print("\n", cart[str(product.id)], "\n")
            # print("\n", cart, "\n")

            # cart[str(product.id)]["product"] = ProductSerializer(product).data
            # cart[str(product.id)]["price"] = product.price
        for item in cart.values():
            # item["price"] = Decimal(item["price"])
            # item["price"] = Decimal(item["price"])
            # item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        return len(self.cart)

    def get_total_price(self):
        print("\n\n", self.cart, "\n\n")
        return sum(
            # Decimal(item["price"]["RUB"]) * item["quantity"] for item in self.cart.values()
            # Decimal(item["product"]["price"]["RUB"]) * item["quantity"]
            Decimal(item["price"]) * item["quantity"]
            for item in self.cart.values()
        )

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()


class RecentViewed:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        recent = self.session.get(settings.RECENT_VIEWED_SESSION_ID, None)
        if recent is None:
            # save an empty recent in session
            recent = self.session[settings.RECENT_VIEWED_SESSION_ID] = {}
        self.recent = recent
