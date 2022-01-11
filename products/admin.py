from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    This class will use list_display for what to display in Product Admin
    """
    list_display = (
        'sku',
        'category',
        'name',
        'platform',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    This class will use list_display for what to display in Category Admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    This class will use list_display for what to display in Review Admin
    """
    list_display = (
        'user_review',
        'rate',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
