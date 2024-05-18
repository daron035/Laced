from django.contrib.auth.signals import (
    user_logged_in,
    user_login_failed,
    user_logged_out,
)
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session

# User = get_user_model()
from django.dispatch import Signal
 
# my_signal = Signal(providing_args=["arg1", "arg2"])
my_signal = Signal()

# from path.to.signals import my_signal
from rest_framework_simplejwt.tokens import AccessToken
from .models import UserAccount
@receiver(my_signal)
def my_signal_handler(sender, cookies, access_token, request, response, arg2, **kwargs):
    sessionid = cookies.get("sessionid")
    print("Sender", sessionid)

    # user_id = AccessToken(access_token)["user_id"]
    # user = UserAccount.objects.get(pk=user_id)
    # print(user)

    # session = Session.objects.get(pk=sessionid)
    update_session(request, access_token)
    # print('wewe',session.get_decoded()["preferences"])

    print("Sender", sessionid)
    print(f"Сигнал получен от {request}, arg1={response}, arg2={arg2}")

def update_session(request, access_token):
    user_id = AccessToken(access_token)["user_id"]
    session_key = request.COOKIES.get("sessionid")
    if not session_key:
        return {"error": "Session ID not found in cookies"}
    
    # try:
    account = UserAccount.objects.get(pk=user_id).account
    session = Session.objects.get(pk=session_key)
    
    session_data = session.get_decoded()
    session_data["preferences"] = {
        "currency_iso": account.currency.iso,
        "currency_id": account.currency.pk,
        "country_iso": account.country.iso,
        "country_name": str(account.country),
        "currency_symbol": account.currency.symbol,
    }

    session.session_data = Session.objects.encode(session_data)
    session.save()

    #     print(23)
    #     # return {"success": "Session updated successfully"}
    # except Session.DoesNotExist:
    #     return {"error": "Session not found"}
    # except Exception as e:
    #     print("Произошла ошибка:", e)
    #     return {"error": "An error occurred while updating the session"}

# def sender_function(arg1, arg2):
#     # ... логика отправителя ...
#     print('IOWQERUOIQWEROUIWRQEIOUQWRIUQWERIOPUQWER8978912347894123')
#     my_signal.send(sender=sender_function, arg1=arg1, arg2=arg2)

# @receiver(user_logged_in)
# def user_logged_in_handler(sender, request, user, **kwargs):
#     print(f"Пользователь {user.email} успешно вошел в систему.")
# @receiver(user_logged_in)
# def log_user_login(sender, request, user, **kwargs):
#     print('user logged in')
# from django.contrib.sessions.models import Session
# from django.contrib.sessions.backends.db import SessionStore
# @receiver(user_logged_in)
# def user_logged_in(sender, request, user, **kwargs):
#     account = user.account
#     country = account.country
#     currency = account.currency
#     country_name = str(country)
#     country_iso = country.iso
#     currency_iso = currency.iso
#     currency_id = currency.pk
#     currency_symbol = currency.symbol

#     session = Session.objects.get(pk=request.COOKIES.get("sessionid"))
#     print('''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''')
#     session["preferences"] = {
#         "currency_iso": currency_iso,
#         "currency_id": currency_id,
#         "country_iso": country_iso,
#         "country_name": country_name,
#         "currency_symbol": currency_symbol,
#     }
#     session.save()
    
#     # session_key = set_session_data(country_iso, currency_iso, country_name, currency_id, currency_symbol)
#     # Session.objects.get(pk=request.COOKIES.get("sessionid"))

#     # # do something with key for example, see when the session started
#     # # session = CustomUserSession.objects.filter(session_key=cached_session_key).first()
#     # session = Session.objects.filter(session_key=cached_session_key).first()
