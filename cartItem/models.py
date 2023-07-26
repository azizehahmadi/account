from django.db import models
from customer.models import Customer
from product.models import Product


class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart_customer")
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
       return self.customer.customer_name + " " + self.customer.customer_last_name



class CartItemDetail(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_product")
    cart_user = models.ForeignKey(CartItem, on_delete=models.CASCADE, related_name="cart_user")

    def __str__(self):
        return self.cart_user.customer.customer_name

