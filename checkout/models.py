import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Create your models here.

class Order(models.Model):
    """
    This class will be migrated into the admin, this will generate
    an order report which will be viewable to the user once they
    have created a user account
    """
    order_number = models.CharField(max_length=32, null=False)
    full_name = models.CharField(max_length=48, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    mob_number = models.CharField(max_length=15, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=30, null=False, blank=False)
    first_address_line = models.CharField(max_length=80, null=False, blank=False)
    second_address_line = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=4.99)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generates a random and unique order number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        """
        updates order total viewable in grand_total
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + self.delivery
        self.save()

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=3, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
