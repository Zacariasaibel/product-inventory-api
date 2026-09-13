from django.urls import path

from .views import (
    ProductCreateAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
)


urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("products/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]