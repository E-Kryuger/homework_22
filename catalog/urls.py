from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail, category_products

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path(
        "category-<str:category_name>/",
        category_products,
        name="category_products",
    ),
    path("product-detail/<int:pk>/", product_detail, name="product_detail"),
]
