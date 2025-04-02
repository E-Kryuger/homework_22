from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")  # наименование
    description = models.TextField(verbose_name="Описание")  # описание

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")  # наименование
    description = models.TextField(verbose_name="Описание")  # описание
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="catalog/images/",
        verbose_name="Изображение",
    )  # изображение
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        related_name="products",
    )  # категория
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
    )  # цена за покупку
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="products", )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # дата создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")  # дата последнего изменения
    is_published = models.BooleanField(
        default=False,
        verbose_name="Статус публикации",
        help_text="Опубликовать продукт",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Contact(models.Model):
    country = models.CharField(
        max_length=60,
        verbose_name="Country",
        help_text="Введите название страны"
    )
    tin = models.CharField(
        max_length=20,
        verbose_name="Tax Identification Number",
        help_text="Введите ИНН"
    )
    address = models.TextField(
        verbose_name="Address",
        help_text="Введите адрес")

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
