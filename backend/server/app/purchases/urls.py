from django.urls import path

from .views import (
    CartAPI,
    CreatePaymentView,
    my_webhook_handler,
)


urlpatterns = [
    path("cart/", CartAPI.as_view(), name="cart"),
    path("payment/", CreatePaymentView.as_view(), name="payment"),
    path("verify/", my_webhook_handler, name="hook"),
    # path("cart_size/", CartAPI.as_view()),
    # path("cart/length/", CartAPI.as_view(), name="cart-length"),
]

# from django.urls import path, include
# from .views import CartAPI
# from rest_framework.routers import DefaultRouter
#
# # Создание маршрутизатора
# router = DefaultRouter()
# # Регистрация CartAPI в маршрутизаторе
# router.register(r"cart", CartAPI, basename="cart")
#
# # Включение маршрутов в urlpatterns
# urlpatterns = [
#     path("", include(router.urls)),
# ]
