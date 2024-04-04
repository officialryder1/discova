from django.contrib import admin
from .models import ShippingAddress, Transaction, Order, Completed_order

admin.site.register(ShippingAddress)
admin.site.register(Transaction)
admin.site.register(Order)
admin.site.register(Completed_order)


