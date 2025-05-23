from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products from fixture files to the database"

    def handle(self, *args, **options):
        # Удаление данных перед загрузкой
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка данный из фикстур
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture files"))
