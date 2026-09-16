from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'city', 'status', 'paid', 'created')
    list_filter = ('status', 'paid', 'created')
    search_fields = ('first_name', 'last_name', 'email', 'transaction_id')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'price', 'quantity')
    search_fields = ('product__name',)
