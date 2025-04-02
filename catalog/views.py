from django.http import Http404

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductForm
from catalog.models import Product, Contact
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_queryset(self):
        return Product.objects.order_by("-created_at")


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # contacts = Contact.objects.order_by("-id")
        # context_data["contact_info"] = contacts[0] if contacts.exists() else None
        return context_data

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Имеется новое сообщение от {name} {phone}: {message}")
        context_data = self.get_context_data()
        context_data["message"] = f"Спасибо, {name}! Сообщение получено :)"
        return self.render_to_response(context_data)


class CategoryProductsListView(ListView):
    model = Product
    template_name = "catalog/category_products.html"
    # Словарь содержащий человеко-читаемые названия категорий
    categories_dict = {
        "mailing-lists": "Рассылки",
        "telegram-bots": "Телеграм Боты",
        "useful-utilities": "Полезные утилиты",
        "plugins": "Плагины",
    }

    def get_queryset(self):
        category_key = self.kwargs.get("category_name")
        self.category_name = self.categories_dict.get(category_key)
        if not self.category_name:
            raise Http404("Category not found")
        return Product.objects.filter(category__name=self.category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category_name
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
