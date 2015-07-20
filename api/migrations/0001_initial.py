# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('add_id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('house_no', models.TextField(max_length=5)),
                ('street_name', models.TextField(max_length=150)),
                ('locality', models.TextField(max_length=150)),
                ('landmark', models.TextField(max_length=150, null=True, blank=True)),
                ('city', models.TextField(max_length=200)),
                ('state_or_province', models.TextField(max_length=150)),
                ('pincode', models.TextField(max_length=10)),
                ('sales_person', models.ForeignKey(related_name='addresses', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('add_id',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('cust_name', models.TextField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=200)),
                ('contact', models.TextField(max_length=10)),
                ('add', models.ForeignKey(default=1, to='api.Address')),
                ('sales_person', models.ForeignKey(related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('cust_id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.TextField(max_length=100)),
                ('cost', models.DecimalField(max_digits=8, decimal_places=2)),
                ('brand', models.TextField(max_length=150)),
                ('sales_person', models.ForeignKey(related_name='products', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('prod_id',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('timestamp', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('trans_id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.DecimalField(max_digits=8, decimal_places=2)),
                ('customer', models.ForeignKey(to='api.Customer')),
                ('product', models.ForeignKey(to='api.Product')),
                (
                'sales_person', models.ForeignKey(related_name='transactions', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('trans_id',),
            },
        ),
    ]
