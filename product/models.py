from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = 'itw_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField(max_length=50, null=True)
    default_price = models.FloatField(default=10, null=True)
    description = models.CharField(max_length=50, null=True)
    deleted = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        db_table = 'itw_product_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=50, null=True)
    product = models.ManyToManyField(Product, related_name='categories')
