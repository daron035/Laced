import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import (
    APIView,
    csrf_exempt,
)

from yookassa import (
    Configuration,
    Payment,
)
from yookassa.domain.notification import (
    WebhookNotificationEventType,
    WebhookNotificationFactory,
)

from app.product.views import get_session_currency
from app.purchases.services.create_payment import create_payment

from .serializers import PaymentSerializer
from .service import Cart


@csrf_exempt
def my_webhook_handler(request):
    # Если хотите убедиться, что запрос пришел от ЮКасса, добавьте проверку:
    # ip = get_client_ip(request)  # Получите IP запроса
    # if not SecurityHelper().is_ip_trusted(ip):
    #     return HttpResponse(status=400)

    if request.method == "POST":
        # Извлечение JSON объекта из тела запроса
        event_json = json.loads(request.body)
        try:
            # Создание объекта класса уведомлений в зависимости от события
            notification_object = WebhookNotificationFactory().create(event_json)
            response_object = notification_object.object
            if (
                notification_object.event
                == WebhookNotificationEventType.PAYMENT_SUCCEEDED
            ):
                some_data = {
                    "paymentId": response_object.id,
                    "paymentStatus": response_object.status,
                }
                # Специфичная логика
                # ...
            elif (
                notification_object.event
                == WebhookNotificationEventType.PAYMENT_WAITING_FOR_CAPTURE
            ):
                some_data = {
                    "paymentId": response_object.id,
                    "paymentStatus": response_object.status,
                }
                # Специфичная логика
                # ...
            elif (
                notification_object.event
                == WebhookNotificationEventType.PAYMENT_CANCELED
            ):
                some_data = {
                    "paymentId": response_object.id,
                    "paymentStatus": response_object.status,
                }
                # Специфичная логика
                # ...
            elif (
                notification_object.event
                == WebhookNotificationEventType.REFUND_SUCCEEDED
            ):
                some_data = {
                    "refundId": response_object.id,
                    "refundStatus": response_object.status,
                    "paymentId": response_object.payment_id,
                }
                # Специфичная логика
                # ...
            elif notification_object.event == WebhookNotificationEventType.DEAL_CLOSED:
                some_data = {
                    "dealId": response_object.id,
                    "dealStatus": response_object.status,
                }
                # Специфичная логика
                # ...
            elif (
                notification_object.event
                == WebhookNotificationEventType.PAYOUT_SUCCEEDED
            ):
                some_data = {
                    "payoutId": response_object.id,
                    "payoutStatus": response_object.status,
                    "dealId": response_object.deal.id,
                }
                # Специфичная логика
                # ...
            elif (
                notification_object.event
                == WebhookNotificationEventType.PAYOUT_CANCELED
            ):
                some_data = {
                    "payoutId": response_object.id,
                    "payoutStatus": response_object.status,
                    "dealId": response_object.deal.id,
                }
                # Специфичная логика
                # ...
            else:
                # Обработка ошибок
                return HttpResponse(status=400)  # Сообщаем кассе об ошибке

            # Специфичная логика
            # ...
            Configuration.configure(
                "391979",
                "test_pkOJTPMf2oKAM_oGPtaIue-v51BEhUcCZ1zL6gAwr4g",
            )
            # Получим актуальную информацию о платеже
            payment_info = Payment.find_one(some_data["paymentId"])
            if payment_info:
                payment_status = payment_info.status
                # Специфичная логика
                # ...
                print("payment handler is worked")
                print(payment_status)
                print(payment_info)
            else:
                # Обработка ошибок
                return HttpResponse(status=400)  # Сообщаем кассе об ошибке

        except Exception:
            # Обработка ошибок
            return HttpResponse(status=400)  # Сообщаем кассе об ошибке

    return HttpResponse(status=200)  # Сообщаем кассе, что все хорошо


class CreatePaymentView(APIView):
    def post(self, request):
        print("\n\n", request.data, "\n\n")
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # token = serializer.validated_data["token"]
            # amount = serializer.validated_data["amount"]
            serialized_data = serializer.validated_data

            print("\n\n", "AKLSDGHJUHERGHIERGKSADFJAASDFASJDFHLKAJHSD", "\n\n")
            # print(serialized_data.get("amount", "token"))
            create_payment(serialized_data)
            # print("32323", res.confirmation.confirmation_url)

            # Здесь нужно выполнить запрос к YooKassa API, чтобы совершить платеж по токену.
            # Для примера:
            # headers = {'Authorization': 'Bearer YOUR_YOOKASSA_SECRET_KEY'}
            # data = {'amount': amount, 'token': token}
            # response = requests.post('YOOKASSA_API_ENDPOINT', headers=headers, data=data)

            # После успешного выполнения платежа, обновите баланс пользователя:
            # balance = Balance.objects.get(user=request.user)
            # balance.balance += amount
            # balance.save()

            # a = JsonResponse({"sessionId": confirmation_url["id"]})
            # print("\n\n", a, "\n\n")

            return Response({"message": "Payment successful!"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CartAPI(APIView):
    """Single API to handle cart operations."""

    # def get_serializer_context(self):
    #     """
    #     Этот метод предоставляет контекст для сериализатора.
    #     """
    #     return {
    #         'request': self.request,
    #         'format': self.format_kwarg,
    #         'view': self
    #     }

    def get_serializer_context(self):
        # context = super().get_serializer_context()
        context = {}
        currency = get_session_currency(self.request)
        if currency is not None:
            context["preferences.currency__id"] = currency["id"]
            context["preferences.currency__symbol"] = currency["symbol"]
            context["preferences.currency__iso"] = currency["iso"]
        return context

    def get(self, request, format=None):
        # return Response(status=status.HTTP_200_OK)
        # context = self.get_serializer_context()
        cart = Cart(request)
        # print(request.session["preferences"])
        print("🫥")
        print(request.session["cart"])

        print(1)
        if len(cart) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
            # return Response({"data": None}, status=status.HTTP_200_OK)
            return Response({None}, status=status.HTTP_200_OK)
        print()
        print(2)
        a = cart.get_total_price()
        return Response(
            {
                "data": list(iter(cart)),
                # "cart": cart.data(),
                "count": len(cart),
                "currency": a[0],
                "cart_total_price": cart.get_total_price()[1],
            },
            status=status.HTTP_200_OK,
            # status=status.HTTP_202_ACCEPTED,
        )

    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            product_id = request.data["product_id"]
            variation_id = request.data["variation_id"]
            cart.remove(product_id, variation_id)
            return Response({"message": "Item removed"}, status=status.HTTP_200_OK)
        elif "clear" in request.data:
            cart.clear()
            return Response(
                {"message": "Cart is cleared"},
                status=status.HTTP_205_RESET_CONTENT,
            )
        else:
            product = request.data
            try:
                added_item = cart.add(
                    product_id=product["product_id"],
                    variation_id=product["variation_id"],
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
                    {"message": str(e)},
                    status=status.HTTP_208_ALREADY_REPORTED,
                )
        # return Response({"message": "cart updated"}, status=status.HTTP_200_OK)
        return Response(added_item)
        return Response(
            {
                "data": list(iter(cart)),
                # "cart": cart.data(),
                "count": len(cart),
                # "cart_total_price": cart.get_total_price(),
            },
            status=status.HTTP_200_OK,
            # status=status.HTTP_202_ACCEPTED,
        )
        # Now, set the CORS header before returning the response
        response = Response({"message": "cart updated"}, status=status.HTTP_200_OK)
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    def delete(self, request, **kwargs):
        cart = Cart(request)

        # if "clear" in request.data:
        #     cart.clear()
        #     return Response(
        #         {"message": "Cart is cleared"}, status=status.HTTP_205_RESET_CONTENT
        #     )

        product_id = request.data["product_id"]
        variation_id = request.data["variation_id"]
        i = cart.remove(product_id, variation_id)
        return Response(int(i), status=status.HTTP_200_OK)

        cart = Cart(request)

        if "remove" in request.data:
            product_id = request.data["product_id"]
            variation_id = request.data["variation_id"]
            cart.remove(product_id, variation_id)
            return Response({"message": "Item removed"}, status=status.HTTP_200_OK)


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
