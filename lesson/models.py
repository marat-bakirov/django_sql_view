from decimal import Decimal

from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=50, help_text='Name of type product')


class Product(models.Model):
    name = models.CharField(max_length=50, help_text='The product name')
    description = models.TextField(max_length=50, help_text='Product description')
    price = models.DecimalField(null=True, default=Decimal(0), decimal_places=2, max_digits=10)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']


class ProductTypeSumm(models.Model):
    name = models.CharField(max_length=50, help_text='Name of type product')
    sum = models.DecimalField(null=True, default=Decimal(0), decimal_places=2, max_digits=10)

    class Meta:
        managed = False
        db_table = 'product_type_summ'
