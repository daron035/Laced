from django.contrib.sessions.models import Session

"""https://docs.djangoproject.com/en/dev/topics/http/sessions/#using-sessions-out-of-views"""


class AnonymousUserTrackingMiddleware:
    """
    Adds a session key for anonymous users
    This should be placed after the
    SessionMiddleware but before AuthenticationMiddleware
    """

    def __init__(self, get_response):
        self.get_response = get_response

    # def __call__(self, request):
    #     response = self.get_response(request)
    #     # print("\n", Session.objects.all())
    #     # if not request.session or not request.session.session_key:
    #     # request.session["locale"] = request.LANGUAGE_CODE
    #     # request.session.create()
    #     # if request.user.is_anonymous:
    #     if request.user.is_anonymous:
    #         #     print("WERUIURWEUUWEWREIURWIEREWRWRJ")
    #         request.session.create()
    #     #     has_key = request.session.get("cached_session_key", None)
    #     #     if has_key is None:
    #     #         request.session["cached_session_key"] = request.session.session_key
    #     # print("MID", request.session["cached_session_key"])
    #     # print(request.session.items())
    #     print("MID", request.session.session_key)
    #     # request.session.clear_expired()
    #     # print("COOKIE", request.COOKIES)
    #     return response
    def __call__(self, request):
        if request.session.get("cached_session_key") is None:
            request.session["cached_session_key"] = request.session.session_key
            # if c is None:
            print(999999)
        response = self.get_response(request)
        # c = request.session.get("cached_session_key")
        # if request.session.get("cached_session_key") is None:
        #     request.session["cached_session_key"] = request.session.session_key
        #     # if c is None:
        #     print(999999)
        return response


"""signals.py => settings.py, apps.py:
class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.user"
    # https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-receiver-functions
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals

        # Explicitly connect a signal handler.
        # request_finished.connect(signals.user_signed_up)
"""
