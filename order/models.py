from django.db import models
from customer.models import Customer
from product.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='کاربر', related_name="customer_order")
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return self.customer.customer_name


    class Meta:
        verbose_name= 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول', related_name="order_product")
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبد های خرید'
