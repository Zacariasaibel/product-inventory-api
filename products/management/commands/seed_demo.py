from django.core.management.base import BaseCommand
from django.db import transaction
from products.models import Product, Stock

class Command(BaseCommand):
    help = "Add three fictional products without changing existing records."

    @transaction.atomic
    def handle(self, *args, **options):
        for name, price, quantity in [
            ("Demo-Tastatur", "49.90", 8),
            ("Demo-Maus", "24.90", 12),
            ("Demo-Kopfhörer", "59.90", 0),
        ]:
            product, created = Product.objects.get_or_create(name=name, defaults={
                "short_description": "Fiktiver Artikel zum Testen der API.",
                "product_description": "Kein echtes Angebot. Nur für die Portfolio-Demo.",
                "price": price,
            })
            if created:
                Stock.objects.create(product=product, quantity=quantity)
        self.stdout.write("Fictional examples ready; existing records unchanged.")
