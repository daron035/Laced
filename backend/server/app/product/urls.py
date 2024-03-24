from django.urls import path
from rest_framework import routers

from .views import ProductViewSet


class MyCastomRouter(routers.DefaultRouter):
    routes = [
        routers.Route(
            url=r"^{prefix}/$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        routers.Route(
            url=r"^{prefix}/{lookup}/$",
            mapping={"get": "retrieve"},
            name="{basename}-group-list",
            detail=False,
            initkwargs={"suffix": "Group list"},
        ),
    ]


product_router = MyCastomRouter()
product_router.register(r"product", ProductViewSet, basename="product")
print()
print(product_router.urls)
print()

# urlpatterns = [path("", product_router.urls)]
