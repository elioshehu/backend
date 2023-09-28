from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = 'itw_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField(max_length=50)
    default_price = models.FloatField(default=10)
    description = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)


class Category(models.Model):
    class Meta:
        db_table = 'itw_product_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, related_name='categories')
