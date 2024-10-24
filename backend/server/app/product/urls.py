from django.urls import path
from rest_framework.routers import (
    DefaultRouter,
    DynamicRoute,
    Route,
)

from .session_views import (
    create_session,
    preferences,
)
from .views import ProductViewSet


class MyCastomRouter(DefaultRouter):
    routes = [
        Route(
            url=r"^{prefix}/$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        DynamicRoute(
            url=r"^{prefix}/{url_path}/$",
            name="{basename}-{url_name}",
            detail=False,
            initkwargs={},
        ),
        Route(
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
urlpatterns = [
    path("cookie/", create_session),
    path("preferences/", preferences),
]
