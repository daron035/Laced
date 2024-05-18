from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from app.product.serializers import ProductSerializer
from app.product.models import Product

from .service import Cart, RecentViewed


class CartAPI(APIView):
    """
    Single API to handle cart operations
    """

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
        cart = Cart(request)

        print(1)
        if len(cart) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
            # return Response({"data": None}, status=status.HTTP_200_OK)
            return Response({None}, status=status.HTTP_200_OK)
        print(2)
        return Response(
            {
                "data": list(iter(cart)),
                "count": len(cart),
                "cart_total_price": cart.get_total_price(),
            },
            status=status.HTTP_200_OK,
            # status=status.HTTP_202_ACCEPTED,
        )

    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            product = request.data["id"]
            cart.remove(product)
            return Response(
                {"message": "Item removed"}, status=status.HTTP_202_ACCEPTED
            )
        elif "clear" in request.data:
            cart.clear()
            return Response(
                {"message": "Cart is cleared"}, status=status.HTTP_205_RESET_CONTENT
            )
        else:
            product = request.data
            try:
                cart.add(
                    product_item_id=product["id"],
                    quantity=1,
                    # quantity=product.get("quantity", 1),
                    overide_quantity=(
                        product["overide_quantity"]
                        if "overide_quantity" in product
                        else False
                    ),
                )
            except ValueError as e:
                # return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    {"message": str(e)}, status=status.HTTP_208_ALREADY_REPORTED
                )
        return Response({"message": "cart updated"}, status=status.HTTP_200_OK)
        # Now, set the CORS header before returning the response
        response = Response({"message": "cart updated"}, status=status.HTTP_200_OK)
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    def delete(self, request, **kwargs):
        cart = Cart(request)

        if "clear" in request.data:
            cart.clear()
            return Response(
                {"message": "Cart is cleared"}, status=status.HTTP_205_RESET_CONTENT
            )

        product = request.data["id"]
        cart.remove(product)
        return Response({"message": "Item removed"}, status=status.HTTP_202_ACCEPTED)


#
#
# class RecentVeiwedAPI(APIView):
#
#     def get(self, request, format=None):
#         cart = RecentViewed(request)
#
#         return Response(
#             {"data": list(cart.__iter__()), "cart_total_price": cart.get_total_price()},
#             status=status.HTTP_200_OK,
#         )
