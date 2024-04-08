from django.urls import path
from .views import *

urlpatterns = [
    path('signup', signup, name='merchant-signup'),
    path('admin/unique/dashboard', dashboard, name='dashboard'),
    path('merchant_dashboard', merchant_dashboard, name='merchant_dashboard'),
    path('order', get_order, name='order'),
    path('product', merchant_product, name='product'),
    path("send_feedback", send_message, name="send-message")

]
