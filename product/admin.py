from django.contrib import admin
from product.models import Product, ProductTag, ProductBrand



admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(ProductBrand)