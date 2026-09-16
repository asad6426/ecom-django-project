from django.contrib import admin

from .models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'created')
    list_filter = ('rating',)
    search_fields = ('product__name', 'user__username', 'comment')
