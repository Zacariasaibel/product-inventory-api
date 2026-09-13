from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    Returns all products for the shop homepage.

    This endpoint does not receive URL parameters.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns, updates or deletes one product.

    The product ID is received through the URL as the parameter 'pk'.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Creates a new product.

    Product data is received in the JSON body of a POST request.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer