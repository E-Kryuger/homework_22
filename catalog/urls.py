from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsTemplateView, CategoryProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "category-<str:category_name>/",
        CategoryProductsListView.as_view(),
        name="category_products",
    ),
    path("product-create/", ProductCreateView.as_view(), name="product_create"),
    path("product-detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product-update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product-delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
