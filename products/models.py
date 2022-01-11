from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=256)
    friendly_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=256)
    age_rating = models.CharField(max_length=10, null=True, blank=True)
    platform = models.CharField(max_length=256, null=True, blank=True)
    genre = models.CharField(max_length=256, null=True, blank=True)
    sizes = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


ONE_TO_FIVE = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user_review = models.TextField(max_length=500, blank=True)
    rate = models.PositiveSmallIntegerField(choices=ONE_TO_FIVE)

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)