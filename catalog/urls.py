from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsTemplateView, CategoryProductsListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "category-<str:category_name>/",
        CategoryProductsListView.as_view(),
        name="category_products",
    ),
    path("product-detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
