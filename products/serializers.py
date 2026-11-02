from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from .models import Product, Stock

class ProductSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source="stock.quantity", min_value=0)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal("0.00"))

    class Meta:
        model = Product
        fields = ["id", "name", "short_description", "product_description", "stock", "price"]

    @transaction.atomic
    def create(self, validated_data):
        stock_data = validated_data.pop("stock")
        product = Product.objects.create(**validated_data)
        Stock.objects.create(product=product, **stock_data)
        return product

    @transaction.atomic
    def update(self, instance, validated_data):
        stock_data = validated_data.pop("stock", None)
        if stock_data is not None:
            stock, _ = Stock.objects.update_or_create(product=instance, defaults=stock_data)
            instance.stock = stock
        return super().update(instance, validated_data)
