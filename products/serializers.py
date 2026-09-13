from rest_framework import serializers

from .models import Product, Stock


class ProductSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source="stock.quantity")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "short_description",
            "product_description",
            "stock",
            "price",
        ]

    def create(self, validated_data):
        stock_data = validated_data.pop("stock")
        product = Product.objects.create(**validated_data)
        Stock.objects.create(product=product, **stock_data)
        return product

    def update(self, instance, validated_data):
        stock_data = validated_data.pop("stock", None)

        if stock_data is not None:
            instance.stock.quantity = stock_data["quantity"]
            instance.stock.save()

        return super().update(instance, validated_data)