from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete


class Country(models.Model):
    COUNTRY_CHOICES = [
        ("RU", "Russian Federation"),
        ("KZ", "Kazakhstan"),
        ("BY", "Belarus"),
    ]
    value = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default="RU")

    def __str__(self):
        return self.get_value_display()

    class Meta:
        verbose_name_plural = "Countries"

    @classmethod
    def get_default_pk(cls):
        country, created = cls.objects.get_or_create(
            value="RU",
            # defaults=dict(description='this is not an exam'),
        )
        return country.pk


class Currency(models.Model):
    CURRENCY_CHOICES = [
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("RUB", "Russian Ruble"),
        ("KZT", "Kazakhstani Tenge"),
        ("BYN", "Belarusian Ruble"),
    ]
    value = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="RUB")

    def __str__(self):
        return self.get_value_display()

    class Meta:
        verbose_name_plural = "Currencies"

    @classmethod
    def get_default_pk(cls):
        currency, created = cls.objects.get_or_create(
            value="RUB",
            # defaults=dict(description='this is not an exam'),
        )
        return currency.pk

    # def __str__(self):
    #     return self.user.username !WRONG


class Account(models.Model):
    LOCALE_CHOICES = [
        ("ru", "Russian"),
        ("en", "English"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    profile_complete = models.BooleanField(default=False)
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.SET_DEFAULT,
        default=Currency.get_default_pk,
        related_name="preferred_currency",
    )
    location = models.ForeignKey(
        "Country",
        on_delete=models.SET_DEFAULT,
        default=Country.get_default_pk,
        related_name="preferred_location",
    )
    # locale = models.CharField(max_length=2, choices=LOCALE_CHOICES, default="ru")
    locale = models.CharField(
        max_length=2, choices=LOCALE_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return str(self.user)

    # "email": "kamil249@mail.ru",
    # "first_name": "Камил",
    # "last_name": "Кусяков",
    # "role": "customer",
    # "permissions": [],
    # "country": "GB",
    # "dob": "2000-01-01",
    # "phone_number": "9279453342",
    # "dialing_code": "+44",
    # "billing_address_id": 795574,
    # "preferred_locale": "en",
    # "preferred_currency": "EUR",
    # "preferred_location": "GB",
    # "preferred_auth_centre_id": null,
    # "seller_type": "private",
    # "profile_complete": true,
    # "seller_profile_complete": true,
    # "selling_count": 0,
    # "sold_count": 1,
    # "purchase_count": 0,
    # "stripe_connected_account_region": "uk",
    # "stripe_uid": "acct_1MZzrVFtHYGiM2Qn",
    # "isStaff": false


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # currency = Currency.objects.get(pk=1)
        # location = Country.objects.get(pk=1)
        # user_profile = Account(user=instance, currency=currency, location=location)
        user_profile = Account(user=instance)
        user_profile.save()


# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# @receiver(user_logged_in)
# def user_logged_in_handler(sender, request, user, **kwargs):
#     # print(f"Пользователь {user.username} успешно вошел в систему.")
#     print(f"Пользователь  успешно вошел в систему.")
