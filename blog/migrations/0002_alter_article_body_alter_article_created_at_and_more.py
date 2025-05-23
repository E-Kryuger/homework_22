# Generated by Django 5.1.2 on 2025-03-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="body",
            field=models.TextField(help_text="Введите содержимое статьи", verbose_name="Содержимое"),
        ),
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="article",
            name="is_published",
            field=models.BooleanField(default=False, help_text="Опубликовать статью", verbose_name="Дата публикации"),
        ),
        migrations.AlterField(
            model_name="article",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="blog/images/", verbose_name="Превью"),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(help_text="Введите заголовок статьи", max_length=250, verbose_name="Заголовок"),
        ),
        migrations.AlterField(
            model_name="article",
            name="views_counter",
            field=models.PositiveIntegerField(
                default=0, help_text="Накрутить количество просмотров", verbose_name="Счётчик просмотров"
            ),
        ),
    ]
