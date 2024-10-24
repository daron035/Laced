

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # lang_code1 = get_language_from_request(request)
        # lang_code2 = request.LANGUAGE_CODE

        # locale = request.COOKIES.get("locale", "en")
        # locale = request.COOKIES.get("NEXT_LOCALE", "en")
        # self.session = request.session
        # cart = self.session.get("account", None)
        # locale = request.COOKIES
        # request.locale = locale
        # print("locale", locale)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
