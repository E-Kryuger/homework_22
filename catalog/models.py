from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # дата создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")  # дата последнего изменения

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
