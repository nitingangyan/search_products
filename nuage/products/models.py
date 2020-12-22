from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.IntegerField(default=None, null=True, blank=True)
    name = models.CharField(max_length=300)
    url = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)