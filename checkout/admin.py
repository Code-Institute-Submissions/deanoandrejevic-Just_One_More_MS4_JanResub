from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    This is the details of what the admin will see in
    the admin page
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'mob_number',  'first_address_line',
              'second_address_line', 'city', 'county',
              'postcode', 'country', 'delivery',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
