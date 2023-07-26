from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="عنوان")
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال', default=False)
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده', null=True)

    def __str__(self):
        return self.title

