from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
       
class Stock(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="stock",
    )
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.product.name}: {self.quantity}"
    
    

