from django.contrib import admin
from django.urls import include, path

from app.user.urls import user_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += user_urlpatterns
