
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.views.generic import ListView, DetailView, CreateView

# from app.cart.models import Cart
from app.product.models import Product, Category
from .forms import AddProductForm


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


def index3(request):
    product = Product.objects.all()

    insert_content = {
        "product": product,
        # 'menu': menu,
        # 'title': 'Главная страница',
        # 'cat_selected': 0,
    }

    return render(request, "management/index.html", context=insert_content)


class ProductView(ListView):
    model = Product
    template_name = "management/contacts.html"
    context_object_name = "products"
    paginate_by = 20
    # extra_context = {'title': 'Главная страница'} # просто контекст статичный, мусорный

    def get_context_data(self, *, object_list=None, **kwargs):
        a = self.request.session.session_key
        # a = self.request.session.items()
        print(a)
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Главная страница")
        # context и c_def формируют общий нужный context
        # context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):  # фильтруем посты из модели Women
        return Product.objects.all()


# class AddProductView(LoginRequiredMixin, CreateView):
class AddProductView(LoginRequiredMixin, FormView):
    form_class = AddProductForm
    template_name = "management/add_product.html"
    # success_url = reverse_lazy('home') reverse в отличие от revers_lazy, сразу пытается построить маршрут
    # в момент создания экземпляра класса
    # если не указывать этот свойство, то автоматически перенапрправится по get_ lute_url
    login_url = reverse_lazy("home")
    # login_url = '/admin/' # перенаправление неавторизованных пользователей на страницу админки
    raise_exception = True  # перенаправление на страницу 403

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["types"] = Category.objects.filter(type=Category.ProductType.TYPE)
        # context["brands"] = Category.objects.filter(type=Category.ProductType.BRAND)
        # context["series"] = Category.objects.filter(type=Category.ProductType.MODEL)
        # c_def = self.get_user_context(title='Добавление статьи')
        # context = dict(list(context.items()) + list(c_def.items()))
        return context


def search_product(request):
    search_text = request.POST.get('search')
    results = Category.objects.filter(name__icontains=search_text)
    context = {'results': results}
    return render(request, 'management/search-results.html', context)

# def load_options(request):
#     cat_id = request.GET.get("type") or request.GET.get("brand")
#     brands = Category.objects.filter(parent_category_id=cat_id)
#     return render(request, "management/brand_options.html", {"brands": brands})

def load_brands(request):
    cat_id = request.GET.get("type")
    brands = Category.objects.filter(parent_category_id=cat_id)
    return render(request, "management/brand_options.html", {"brands": brands})

def load_series(request):
    cat_id = request.GET.get("brand")
    brands = Category.objects.filter(parent_category_id=cat_id)
    return render(request, "management/brand_options.html", {"brands": brands})
