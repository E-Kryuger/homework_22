from django.contrib import admin
from .models import Product, Category


# Для Category выведите id и name в списке
# Для Product выведите id, name, price и category в списке
# Настройте фильтрацию продуктов по категории
# Настройте поиск по полям name и description


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")
