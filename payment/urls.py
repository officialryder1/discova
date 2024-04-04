from django.urls import path
from .views import *

urlpatterns = [
   path('payment_success', payment_success, name='payment_success'),
   path("shipping_form", shipping_form, name='checkout_form'),
   path('checkout', checkout, name='checkout'),
   path('update_shipping', update_info, name='update_info')
]
