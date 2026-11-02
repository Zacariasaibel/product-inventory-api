from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from products.models import Product

class Command(BaseCommand):
    help = "Restore fictional products only in the isolated demo environment."

    @transaction.atomic
    def handle(self, *args, **options):
        if not getattr(settings, "DEMO_MODE", False):
            raise CommandError("Use config.demo_settings; personal databases cannot be reset.")
        Product.objects.all().delete()
        call_command("seed_demo", stdout=self.stdout)
