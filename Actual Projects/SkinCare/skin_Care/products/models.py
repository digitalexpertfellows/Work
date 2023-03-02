from django.db import models

# Create your models here.

PRODUCT_CHOICES = (
    ("Face Cream", "1"),
    ("Hands Cream", "2"),
    ("Body Cream", "3"),
)

class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_description = models.TextField(max_length=320)
    rating = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(
        max_length=50,
        choices=PRODUCT_CHOICES,
        default="1"
    )


    def __str__(self):
        return f"{self.product_name}"