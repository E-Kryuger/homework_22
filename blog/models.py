from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок", help_text="Введите заголовок статьи")
    body = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое статьи")
    preview = models.ImageField(blank=True, null=True, upload_to="blog/images/", verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Дата публикации", help_text="Опубликовать статью")
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        default=0,
        help_text="Накрутить количество просмотров",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
        ordering = ["-created_at"]
