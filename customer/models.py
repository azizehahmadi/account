from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=500)
    customer_last_name = models.CharField(max_length=500)
    customer_address = models.CharField(max_length=500)
    customer_post_code = models.IntegerField()
    customer_phone = models.IntegerField()

    def __str__(self):
        return self.customer_name + " " + self.customer_last_name
