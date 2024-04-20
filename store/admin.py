from django.contrib import admin
from .models import Category, Product, CompanyProfile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CompanyProfile)
