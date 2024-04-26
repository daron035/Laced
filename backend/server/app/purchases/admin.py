from django.contrib import admin

from .models import Account, Country, Currency


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "balance", "currency", "country")
    ordering = ("id",)
    list_display_links = ("id", "user")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "iso")
    ordering = ("id",)
    list_display_links = ("id", "iso")


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "iso", "symbol")
    ordering = ("id",)
    list_display_links = ("id", "iso")
