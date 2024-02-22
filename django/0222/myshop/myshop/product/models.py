from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_count = models.IntegerField(default=0)
    img_path = models.CharField(max_length=200, default='img/product/product_1.png')