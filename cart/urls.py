from django.urls import path
from .views import *

urlpatterns = [
   path('', cart_info, name='cart'),
   path('add', add, name='add'),
   path('update', edit, name='edit'),
   path('delete', delete, name='delete')
]
