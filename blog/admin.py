from django.contrib import admin
from .models import Shops, Products, Manufactures, ShopsAndProducts, ProductsAndManufactures

admin.site.register(Shops)
admin.site.register(Products)
admin.site.register(Manufactures)
admin.site.register(ShopsAndProducts)
admin.site.register(ProductsAndManufactures)