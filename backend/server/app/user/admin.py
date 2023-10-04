from django.contrib import admin
from .models import UserAccount


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        # "date_joined",
    ]
    list_display_links = [
        "id",
        "first_name",
    ]


admin.site.register(UserAccount, UserAdmin)
