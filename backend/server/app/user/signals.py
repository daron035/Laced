from django.contrib.auth.signals import (
    user_logged_in,
    user_login_failed,
    user_logged_out,
)
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session

# User = get_user_model()


# @receiver(user_logged_in)
# def user_logged_in_handler(sender, request, user, **kwargs):
#     print(f"Пользователь {user.email} успешно вошел в систему.")


@receiver(user_logged_in)
def user_logged_in(sender, request, user, **kwargs):
    cached_session_key = request.session.get("cached_session_key")
    print("\n", "cached_session_key", cached_session_key, "\n")

    # do something with key for example, see when the session started
    # session = CustomUserSession.objects.filter(session_key=cached_session_key).first()
    session = Session.objects.filter(session_key=cached_session_key).first()
