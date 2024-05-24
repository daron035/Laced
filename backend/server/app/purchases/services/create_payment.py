import json
import uuid
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
from yookassa import Configuration, Payment

# from ..models import Balance, BalanceChange

# Configuration.configure("983923", "test_RRm3ODuDVDOmdzikoM_GWxx4pOZ-GNxlzgV7OMOmtGk")
Configuration.configure("391979", "test_pkOJTPMf2oKAM_oGPtaIue-v51BEhUcCZ1zL6gAwr4g")

userok = get_user_model()


# idempotence_key = str(uuid.uuid4())
idempotence_key = uuid.uuid4()
from pprint import pprint


def create_payment(serialized_data):
    token = serialized_data.get("token")
    amount = serialized_data.get("amount")
    user = userok.objects.get(pk=1)

    # balance = Balance.objects.get_or_create(user=user)
    # balance = Balance.objects.get(pk=1)

    # change = BalanceChange.objects.create(
    #     balance_id=balance, amount=amount, is_accepted=False, operatio_type="DEPOSIT"
    # )
    print("\n\n", "AKLSDGHJUHERGHIERGKSADFJAASDFASJDFHLKAJHSD", "\n\n")

    payment = Payment.create(
        {
            "payment_token": token,
            # "amount": {"value": "2.00", "currency": "RUB"},
            "amount": {"value": amount, "currency": "RUB"},
            # "payment_method_data": {"type": "bank_card"},
            # "payment_token": str(token),
            "confirmation": {
                "type": "redirect",
                # "return_url": "https://www.example.com/return_url",
                # "return_url": "http://127.0.0.1:3000/products",
                "return_url": "https://da7e-178-129-103-40.ngrok-free.app/api/verify/",
            },
            # "capture": False,
            "capture": True,
            "description": "ZakaZ #724",
        },
        idempotence_key,
    )
    print("\n\n", "148129374891273401982734819273401897243819", "\n\n")

    # get confirmation url
    # confirmation_url = payment.confirmation.confirmation_url
    # print(payment.confirmation.confirmation_url)
    # return payment.confirmation.confirmation_url
    # print(payment.__dict__)
    # confirmation_url = payment.confirmation.confirmation_url
    # confirmation_url = payment.confirmation.type
    # print("23", confirmation_url)
    # print(payment.id)
    # print(dir(payment))
    # print("\n\n", payment.confirmation, "\n\n")
    # print("\n\n", payment.status, "\n\n")
    print("\n\n", payment.status)
    print(payment.amount.value, "\n\n")
    # print(payment.confirmation["confirmation_url"], "\n\n")
    # print(payment.data, "\n\n")

    pprint(payment)
    # print(vars(payment))
    # print("\n\n", JSONRenderer().render(payment.data), "\n\n")
    return payment
