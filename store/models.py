from django.db import models
from django.contrib.auth.models import User
from merchant.models import Merchant


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    owner = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    specification = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    location = models.CharField(max_length=50)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name +' - '+ str(self.stock)
        
    @property
    def line_total(self):
        return self.stock * self.price

