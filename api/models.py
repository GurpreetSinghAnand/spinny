from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True, auto_created=True)
    display_name = models.TextField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.TextField(max_length=150)
    sales_person = models.ForeignKey(User, related_name='products', default=1)

    class Meta:
        ordering = ('prod_id',)


class Address(models.Model):
    add_id = models.AutoField(primary_key=True, auto_created=True)
    house_no = models.TextField(max_length=5)
    street_name = models.TextField(max_length=150)
    locality = models.TextField(max_length=150)
    landmark = models.TextField(max_length=150, blank=True, null=True)
    city = models.TextField(max_length=200)
    state_or_province = models.TextField(max_length=150)
    pincode = models.TextField(max_length=10)
    sales_person = models.ForeignKey(User, related_name='addresses', default=1)

    # @property
    # def full_address(self):
    #     return str(self.house_no)+',\n'+str(self.street_name)+',\n'+str(self.locality)+',\n'+str(self.landmark)+',\n'+str(self.city)+',\n'+str(self.state_or_province)+',\n'+str(self.pincode)

    class Meta:
        ordering = ('add_id',)


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True, auto_created=True)
    cust_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    contact = models.TextField(max_length=10)
    sales_person = models.ForeignKey(User, related_name='customers')
    add = models.ForeignKey(Address, related_name='customers', default=1)

    class Meta:
        ordering = ('cust_id',)


class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True, auto_created=True)
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    sales_person = models.ForeignKey(User, related_name='transactions', default=1)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_created=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = ('trans_id',)
