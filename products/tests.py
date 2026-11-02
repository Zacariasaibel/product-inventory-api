from io import StringIO
from unittest.mock import patch
from django.core.management import call_command
from django.core.management.base import CommandError
from django.db import IntegrityError
from django.test import TestCase, override_settings
from rest_framework.test import APITestCase
from .models import Product, Stock
from .serializers import ProductSerializer

class ProductAPITests(APITestCase):
    def setUp(self):
        self.data = {"name": "Demo", "short_description": "Fictional", "product_description": "Demo only", "price": "12.50", "stock": 4}

    def create_product(self):
        response = self.client.post("/api/products/create/", self.data, format="json")
        self.assertEqual(response.status_code, 201)
        return f"/api/products/{response.data['id']}/"

    def test_complete_crud(self):
        url = self.create_product()
        self.assertEqual(self.client.get("/api/products/").data[0]["stock"], 4)
        self.assertEqual(self.client.get(url).data["price"], "12.50")
        response = self.client.put(url, {**self.data, "name": "Changed", "stock": 2}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["stock"], 2)
        response = self.client.patch(url, {"price": "0.00"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["stock"], 2)
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(Stock.objects.count(), 0)

    def test_negative_stock_and_price_rejected_without_writes(self):
        for field, value in [("stock", -1), ("price", "-0.01"), ("price", "abc"), ("price", "1.001"), ("stock", 1.5)]:
            with self.subTest(field=field,value=value):
                response = self.client.post("/api/products/create/", {**self.data, field:value}, format="json")
                self.assertEqual(response.status_code, 400)
                self.assertIn(field,response.data)
        self.assertEqual(Product.objects.count(), 0)

    def test_missing_and_blank_fields_rejected(self):
        for data in [{}, {**self.data,"name":" "}, {**self.data,"stock":None}]:
            self.assertEqual(self.client.post("/api/products/create/",data,format="json").status_code,400)

    def test_invalid_patch_preserves_values(self):
        url=self.create_product()
        self.assertEqual(self.client.patch(url,{"stock":-2},format="json").status_code,400)
        self.assertEqual(self.client.get(url).data["stock"],4)

    def test_full_update_requires_fields_and_unknown_product_is_404(self):
        url=self.create_product()
        self.assertEqual(self.client.put(url,{"name":"Missing"},format="json").status_code,400)
        self.assertEqual(self.client.get("/api/products/99999/").status_code,404)

    def test_browsable_renderer_is_available(self):
        response=self.client.get("/api/products/",HTTP_ACCEPT="text/html")
        self.assertEqual(response.status_code,200)
        self.assertIn("text/html",response["Content-Type"])

    def test_stock_can_be_added_to_product_created_in_admin(self):
        product=Product.objects.create(name="Admin Demo",price="1.00",short_description="Demo",product_description="Demo")
        response=self.client.patch(f"/api/products/{product.pk}/",{"stock":3},format="json")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["stock"],3)

    def test_create_rolls_back_if_stock_write_fails(self):
        serializer=ProductSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        with patch("products.serializers.Stock.objects.create",side_effect=IntegrityError("test")):
            with self.assertRaises(IntegrityError):
                serializer.save()
        self.assertEqual(Product.objects.count(),0)

    def test_update_rolls_back_stock_if_product_write_fails(self):
        self.create_product()
        product=Product.objects.first()
        serializer=ProductSerializer(product,data={"stock":2,"name":"Changed"},partial=True)
        self.assertTrue(serializer.is_valid())
        with patch.object(Product,"save",side_effect=IntegrityError("test")):
            with self.assertRaises(IntegrityError):
                serializer.save()
        self.assertEqual(Stock.objects.get(product=product).quantity,4)

class DemoCommandTests(TestCase):
    def test_seed_is_repeatable(self):
        for _ in range(2): call_command("seed_demo",stdout=StringIO())
        self.assertEqual(Product.objects.count(),3)
        self.assertEqual(Stock.objects.count(),3)

    def test_reset_refuses_normal_settings(self):
        with self.assertRaises(CommandError): call_command("reset_demo",stdout=StringIO())

    @override_settings(DEMO_MODE=True)
    def test_reset_restores_demo(self):
        call_command("seed_demo",stdout=StringIO())
        Product.objects.all().delete()
        call_command("reset_demo",stdout=StringIO())
        self.assertEqual(Product.objects.count(),3)
