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

    code = models.IntegerField()
    code_year = models.IntegerField()
    date_registered = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderUnit(models.Model):
    class Meta:
        db_table = 'itw_order_unit'
        verbose_name = 'unit'
        verbose_name_plural = 'units'

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

class Counter(models.Model):
    class Meta:
        db_table = 'itw_counter'
        verbose_name = 'counter'
        verbose_name_plural = 'counters'

    name = models.CharField(max_length=10)
    value = models.IntegerField()