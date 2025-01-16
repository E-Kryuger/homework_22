from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    return render(request, template_name="catalog/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, template_name="catalog/contacts.html")


def category_products(request, category_name):
    """Контроллер для отображения списка продуктов конкретной категории"""
    # Словарь содержащий человеко-читаемые названия категорий
    categories_dict = {
        "mailing-lists": "Рассылки",
        "telegram-bots": "Телеграм Боты",
        "useful-utilities": "Полезные утилиты",
        "plugins": "Плагины",
    }
    # Получение названия категории
    category_name = categories_dict.get(category_name)
    if not category_name:
        raise Http404("Category not found")
    # Фильтрация продуктов по полученному названию категории
    the_products = Product.objects.filter(category__name=category_name)
    context = {
        "category_name": category_name,
        "products": the_products,
    }
    return render(
        request,
        template_name="catalog/category_products.html",
        context=context,
    )


def product_detail(request, pk):
    """Контроллер для отображения страницы с подробной информацией о товаре"""
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        "product_id": pk,
    }
    return render(request, "catalog/product_detail.html", context=context)
