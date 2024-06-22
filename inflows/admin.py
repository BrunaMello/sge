from django.contrib import admin

from inflows import models


# Register your models here.

class InflowAdmin(admin.ModelAdmin):
	list_display = ['product', 'quantity', 'supplier', 'created_at', 'updated_at']
	list_filter = ['product__title', 'supplier__name', 'created_at', 'updated_at']
	search_fields = ['product__title', 'product__title']
	list_per_page = 10


admin.site.register(models.Inflow, InflowAdmin)
