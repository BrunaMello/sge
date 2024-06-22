from django.contrib import admin

from outflows import models


# Register your models here.

class OutflowAdmin(admin.ModelAdmin):
	list_display = ['product', 'quantity', 'created_at', 'updated_at']
	list_filter = ['product__title']
	search_fields = ['product__title']
	list_per_page = 10


admin.site.register(models.Outflow, OutflowAdmin)
