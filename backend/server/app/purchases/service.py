from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import ipinfo
from enum import Enum

from app.product.serializers import ProductSerializer, CartProductSerializer
from app.product.models import Price, Product, ProductItem
from app.product.session_views import get_session_currency


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
        # currency = self.request.session.get("preferences", None)
        currency = get_session_currency(self.request)
        if currency:
            context["preferences.currency__id"] = currency["id"]
            context["preferences.currency__iso"] = currency["iso"]
        return context

    def save(self):
        self.session.modified = True

    def add(self, product_item_id, quantity, overide_quantity=False):
        """
        Add product to the cart or update its quantity
        """
        product_item_id = str(product_item_id)

        prod_item = ProductItem.objects.get(pk=product_item_id)

        # b = Price.objects.filter(product_id=prod_item)
        # a = {"price": b.values()}
        # print("♥️")
        # print(a)
        # preferences = self.session.get("preferences")
        # if preferences:
        #     # print("2323232323", currency)
        #     # print("♥️")
        #     price = Price.objects.filter(
        #         # product=prod_item, currency=preferences["currency_iso"]
        #         product=prod_item
        #     )
        # # # price_item = "{:.2f}".format(float(prod_item.RUB))
        # else:
        #     price = Price.objects.get(product=prod_item, currency=4)
        # #
        if product_item_id in self.cart:
            raise ValueError("Product already exists in the cart.")
        if product_item_id not in self.cart:
            self.cart[product_item_id] = 0
            # self.cart[product_item_id] = {
            #     "quantity": 0,
            #     #         # "price": prod_item.price.RUB,
            #     # "price": float(price.value),
            # }
        #     # self.cart[product_id] = {"quantity": 0, "price": str(product["price"])}
        print(1)
        if overide_quantity:
            # self.cart[product_item_id]["quantity"] = quantity
            self.cart[product_item_id] = quantity
        else:
            # self.cart[product_item_id]["quantity"] += quantity
            self.cart[product_item_id] += quantity
        #
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

    def __iter__(self):
        """
        Loop through cart items and fetch the products from the database
        """
        # {'2': {'quantity': 5, 'price': {'RUB': '1800.00'} }, '3': {'quantity': 5, 'price': '1800.00'}}
        # {'2': {'quantity': 5}, '3': {'quantity': 5}
        # print(self.cart)

        product_ids = self.cart.keys()
        products = ProductItem.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            serializer = CartProductSerializer(
                # product, context={"request": self.request}
                product,
                context=self.get_serializer_context(),
            )
            cart[str(product.id)]["product"] = serializer.data
        for item in cart.values():
            # item["price"] = Decimal(item["price"])
            # item["price"] = item["price"]
            # item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item["quantity"] for item in self.cart.values())

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
