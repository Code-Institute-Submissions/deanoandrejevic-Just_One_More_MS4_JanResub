import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django.models import Product

# Create your models here.

class Order(models.Model):
    order_number = models.Charfield(max_length=48, null=false)
    full_name = models.Charfield(max_length=48, null=false, blank=false)
    email = models.EmailField(max_length=256, null=false, blank=false)
    mob_number = models.Charfield(max_length=15, null=false, blank=false)
    country = models.Charfield(max_length=20, null=false, blank=false)
    postcode = models.Charfield(max=length=15, null=True, blank=True)
    city = models.Charfield(max_length=30, null=false, blank=false)
    first_address_line = models.Charfield(max_length=80, null=false, blank=false)
    second_address_line = models.Charfield(max_length=80, null=false, blank=false)
    county = models.Charfield(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery = models.DecimalField(max_digits=5, decimal_places=2, null=false, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=false, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=false, default=0)


class OrderLineItem(models.Model):

