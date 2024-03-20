from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from app.user.urls import user_urlpatterns
from app.product.urls import product_router

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("i18n/", include("django.conf.urls.i18n")),
#     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
#     # Optional UI:
#     path(
#         "api/schema/swagger-ui/",
#         SpectacularSwaggerView.as_view(url_name="schema"),
#         name="swagger-ui",
#     ),
#     path(
#         "api/schema/redoc/",
#         SpectacularRedocView.as_view(url_name="schema"),
#         name="redoc",
#     ),
# ]
# urlpatterns += i18n_patterns(
#     path("", include("app.management.urls")),
#     path("api/", include(product_router.urls)),
#     prefix_default_language=False,
# )

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("i18n/", include("django.conf.urls.i18n")),
#     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
#     # Optional UI:
#     path(
#         "api/schema/swagger-ui/",
#         SpectacularSwaggerView.as_view(url_name="schema"),
#         name="swagger-ui",
#     ),
#     path(
#         "api/schema/redoc/",
#         SpectacularRedocView.as_view(url_name="schema"),
#         name="redoc",
#     ),
# ]
# urlpatterns += i18n_patterns(
#     path("", include("app.management.urls")),
#     path("api/", include(product_router.urls)),
#     prefix_default_language=False,
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dj/", include("app.management.urls")),
    path("api/", include(product_router.urls)),
    path("api/", include("app.purchases.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += user_urlpatterns
# urlpatterns += product_router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
