from django.contrib import admin

from products import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'serie_number']
	search_fields = ['title']
	list_per_page = 10


admin.site.register(models.Product, ProductAdmin)
