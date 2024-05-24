#
# def create_session(request):
#     return HttpRequest()
#
from django.http import HttpResponse
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from app.user.models import UserAccount
from app.purchases.models import Account, Country, Currency


def get_session_currency(request):
    session_currency = request.session.get("preferences", {})
    currency_id = session_currency.get("currency_id", None)
    currency_symbol = session_currency.get("currency_symbol", None)
    currency_iso = session_currency.get("currency_iso", None)

    return {"id": currency_id, "symbol": currency_symbol, "iso": currency_iso}


def preferences(request):
    print("♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️")
    print(request.session.get("preferences"))
    print(request.COOKIES)
    # print(request.headers)
    print("♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️")
    session_currency = request.session.get("preferences", {})
    country_name = session_currency.get("country_name", None)
    country_iso = session_currency.get("country_iso", None)
    currency_symbol = session_currency.get("currency_symbol", None)
    currency_iso = session_currency.get("currency_iso", None)
    currency = f"{currency_symbol} {currency_iso}"
    return JsonResponse(
        {
            "country": country_name,
            "currency": currency,
            "country_iso": country_iso,
            "currency_iso": currency_iso,
        }
    )


from enum import Enum


class CurrencyEnum(Enum):
    RU = "RUB"
    US = "USD"


@api_view(["GET"])
def create_session(request):
    user = request.user
    refresh_token = request.COOKIES.get("refresh")

    def set_session_data(
        country_iso, currency_iso, country_name, currency_id, currency_symbol
    ):
        session = SessionStore()
        session["preferences"] = {
            "currency_iso": currency_iso,
            "currency_id": currency_id,
            "country_iso": country_iso,
            "country_name": country_name,
            "currency_symbol": currency_symbol,
        }
        session.create()
        return session.session_key

    try:
        if user.is_authenticated:
            account = user.account
            country = account.country
            currency = account.currency
            country_name = str(country)
            country_iso = country.iso
            currency_iso = currency.iso
            currency_id = currency.pk
            currency_symbol = currency.symbol
        elif refresh_token:
            user_id = RefreshToken(refresh_token)["user_id"]
            user = UserAccount.objects.get(pk=user_id)
            account = user.account
            country = account.country
            currency = account.currency
            country_name = str(country)
            country_iso = country.iso
            currency_iso = currency.iso
            currency_id = currency.pk
            currency_symbol = currency.symbol
        else:
            country_iso = request.COOKIES.get("country")
            print(country_iso)
            currency_iso = getattr(CurrencyEnum, country_iso).value
            country = Country.objects.get(iso=country_iso)
            print("1", country)
            currency = Currency.objects.get(iso=currency_iso)
            country_name = str(country)
            currency_id = currency.pk
            currency_symbol = currency.symbol
            print("32320923")

        session_key = set_session_data(
            country_iso, currency_iso, country_name, currency_id, currency_symbol
        )

        response = HttpResponse(status=status.HTTP_200_OK)
        response.set_cookie(
            "sessionid",
            session_key,
            max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
            path=settings.AUTH_COOKIE_PATH,
            secure=settings.AUTH_COOKIE_SECURE,
            httponly=settings.AUTH_COOKIE_HTTP_ONLY,
            samesite=settings.AUTH_COOKIE_SAMESITE,
        )

        return response
    except TokenError:
        session_key = set_session_data("RU", "RUB", "Russian Federation", 4, "₽")

        response = HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        response.set_cookie(
            "sessionid",
            session_key,
            max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
            path=settings.AUTH_COOKIE_PATH,
            secure=settings.AUTH_COOKIE_SECURE,
            httponly=settings.AUTH_COOKIE_HTTP_ONLY,
            samesite=settings.AUTH_COOKIE_SAMESITE,
        )

        return response
    except Exception as e:
        print("Произошла ошибка:", e)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
