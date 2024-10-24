from django.urls import (
    include,
    path,
    re_path,
)

from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
)


user_urlpatterns = [
    path("api/auth/", include("djoser.urls")),
    path("api/auth/jwt/create/", CustomTokenObtainPairView.as_view()),
    path("api/auth/jwt/refresh/", CustomTokenRefreshView.as_view()),
    path("api/auth/jwt/verify/", CustomTokenVerifyView.as_view()),
    path("api/auth/logout/", LogoutView.as_view()),
    re_path(
        r"^api/o/(?P<provider>\S+)/$",
        CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
]
