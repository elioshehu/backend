import datetime

from django.contrib.auth.models import User
from django.db import models

from agent.models import Customer
from product.models import Product


# Create your models here.
class Order(models.Model):
    class Meta:
        db_table = 'itw_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    code = models.CharField(max_length=15, null=True, blank=True)
    code_year = models.IntegerField(default=datetime.date.today().year)
    date_registered = models.DateField(default=datetime.date.today())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')


class OrderUnit(models.Model):
    class Meta:
        db_table = 'itw_order_unit'
        verbose_name = 'unit'
        verbose_name_plural = 'units'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='units')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='units')
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0, blank=True)

    def get_product_name(self):
        return self.product.name
    # def save(self, *args, **kwargs):
    #     self.price = self.product.default_price
    #     super().save(*args, **kwargs)


class Counter(models.Model):
    class Meta:
        db_table = 'itw_counter'
        verbose_name = 'counter'
        verbose_name_plural = 'counters'

    name = models.CharField(max_length=10)
    value = models.IntegerField()

    def __str__(self):
        return self.name

    def get_value(self):
        return self.value
