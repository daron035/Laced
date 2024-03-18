from django.contrib import admin

from .models import Account, Country, Currency


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "balance")
    ordering = ("id",)
    list_display_links = ("id", "user")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "value")
    ordering = ("id",)
    list_display_links = ("id", "value")


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "value")
    ordering = ("id",)
    list_display_links = ("id", "value")
