from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'weight', 'gp_price', 'sp_price')


admin.site.register(Product, ProductAdmin)
