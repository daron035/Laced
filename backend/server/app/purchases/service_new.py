from decimal import Decimal

from django.conf import settings

from app.product.models import Product
from app.product.serializers import ProductSerializer


class Cart:
    def __init__(self, request):
        """Initialize the cart."""
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if cart is None:
            # save an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, id, quantity=1, overide_quantity=False):
        """Add product to the cart or update its quantity."""

        # {'2': {'quantity': 5, 'price': '1800.00'}, '3': {'quantity': 5, 'price': '1800.00'}}
        # print(self.cart)

        product_id = str(id)

        if product_id not in self.cart:
            # print("product_id", product_id)
            print(self.cart)
            item = Product.objects.get(pk=product_id)
            # self.cart[product_id] = {"quantity": 0, "price": str(product["price"])}
            self.cart[product_id] = {"quantity": 0, "price": str(product["price"])}
            # self.cart[product_id] = {"quantity": 0}
        if overide_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product):
        """Remove a product from the cart."""
        product_id = str(product["id"])

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Loop through cart items and fetch the products from the database."""
        # {'2': {'quantity': 5, 'price': '1800.00'}, '3': {'quantity': 5, 'price': '1800.00'}}
        # print(self.cart)

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            # {'quantity': 5, 'price': '1800.00'}
            # print(cart[str(product.id)])

            serializer = ProductSerializer(product, context={"request": self.request})
            cart[str(product.id)]["product"] = serializer.data
            # print("1", cart[str(product.id)]["product"], "\n")
            # print("\n", cart[str(product.id)], "\n")
            # print("\n", cart, "\n")

            # cart[str(product.id)]["product"] = ProductSerializer(product).data
            # cart[str(product.id)]["price"] = product.price
        for item in cart.values():
            # item["price"] = Decimal(item["price"])
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """Count all items in the cart."""
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
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
