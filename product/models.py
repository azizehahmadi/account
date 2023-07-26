from django.db import models
from category.models import Category



class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    category = models.ManyToManyField(Category, related_name='product_categories', verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True,
                              related_name='product_brand')
    price = models.IntegerField(verbose_name="قیمت")
    short_description = models.CharField(null=True, db_index=True, verbose_name="توضیحات کوتاه",max_length=360)
    description = models.TextField(verbose_name="توضیحات اصلی", db_index=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال", null=True)
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده', null=True)
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')


    def __str__(self):
        return f"{self.title}({self.price})"


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان', null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="تگ های محصول", related_name='product_tags',null=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های مجصول'