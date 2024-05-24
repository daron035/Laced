from rest_framework.views import APIView, csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from app.product.serializers import ProductSerializer
from app.product.models import Product
from .serializers import PaymentSerializer
from app.purchases.services.create_payment import create_payment

from .service import Cart, RecentViewed


import json
from django.http import HttpResponse
from yookassa import Configuration, Payment
from yookassa.domain.notification import (
    WebhookNotificationEventType,
    WebhookNotificationFactory,
)
from yookassa.domain.common import SecurityHelper


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
                "391979", "test_pkOJTPMf2oKAM_oGPtaIue-v51BEhUcCZ1zL6gAwr4g"
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
            res = create_payment(serialized_data)
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
    """
    Single API to handle cart operations
    """

    def get(self, request, format=None):
        # return Response(status=status.HTTP_200_OK)
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
                # "cart_total_price": cart.get_total_price(),
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
