from django.urls import path

# from .views import CartAPI, RecentVeiwedAPI
from .views import CartAPI

urlpatterns = [
    path("cart/", CartAPI.as_view(), name="cart"),
    # path("recent_viewed/", RecentVeiwedAPI.as_view(), name="cart"),
]
