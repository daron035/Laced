from django.shortcuts import render
from django.contrib.sessions.models import Session

# from app.cart.models import Cart


from django.contrib.sessions.backends.db import SessionStore


def index(request):
    if not request.session or not request.session.session_key:
        # request.session.create()
        # request.session["cached_session_key"] = request.session.session_key
        request.session.create()
        c = Session.objects.filter(session_key=request.session.session_key).first()
        # b = Cart.objects.get_or_create(session=c)
        # print("B", b)
    else:
        print("0101", request.session.session_key, "0101")

    return render(request, "management/index.html")


def index2(request):
    return render(request, "management/index_jk.html", {})
