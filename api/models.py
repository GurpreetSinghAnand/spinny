from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True, auto_created=True)
    display_name = models.TextField(max_length=100)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    brand = models.TextField(max_length=150)
    sales_person = models.ForeignKey(User, related_name='products', default=1)

    class Meta:
        ordering = ('prod_id',)

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True, auto_created=True)
    cust_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    contact = models.TextField(max_length=10)
    sales_person = models.ForeignKey(User, related_name='customers')
    address = models.TextField(max_length=350, unique=True)

    class Meta:
        ordering = ('cust_id',)


class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True, auto_created=True)
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    sales_person = models.ForeignKey(User, related_name='transactions')
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_time = models.DateTimeField(auto_created=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = ('transaction_time',)
