
from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'name_shop', 'city', 'mobile', 'created', 'products_tag',
        'delivery_method', 'delivery_district_address', 'delivery_region_address',
        'post_office', 'numbers'
    ]

    list_filter = ['numbers', 'delivery_method', 'name_shop', 'mobile']

    def products_tag(self, obj):
        return ', '.join(map(str, obj.items.all()))
