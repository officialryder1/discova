from django.db import models
from store.models import Product
from django.contrib.auth.models import User
from merchant.models import Merchant


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70)
    email = models.CharField(max_length=130, blank=True, null=True)
    number = models.IntegerField()
    address_1 = models.CharField(max_length=130)
    address_2 = models.CharField(max_length=130)
    city = models.CharField(max_length=130)
    state = models.CharField(max_length=130)
    country = models.CharField(max_length=130)


    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.full_name)}'
    

class Order(models.Model):
    user = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order - {str(self.id)}"


class Transaction(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
        ('Review', 'Review'),
        ('Approved', 'Approved')
        
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.FloatField()
    delivery_date = models.DateField(blank=True, null=True)
    coupon = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default="Pending")
    bank_name = models.CharField(default='Zenith Bank', max_length=100, null=True, blank=True)
    acct_no = models.IntegerField(default='2212833276', null=True, blank=True)
    acct_name = models.CharField(default='VICTOR KENNETH', max_length=100, null=True, blank=True)


    def __str__(self):
        return f"Order Item - {str(self.name)}"
    
    
class Completed_order(models.Model):
    user = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class BillingAddress(models.Model):
    pass
