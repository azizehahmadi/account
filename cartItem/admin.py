from django.contrib import admin
from cartItem.models import CartItem, CartItemDetail

admin.site.register(CartItem)
admin.site.register(CartItemDetail)