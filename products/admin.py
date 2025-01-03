from django.contrib import admin
from .models import Product, Category

# Registered models for product app here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'image',
        'rating',
    )

    ordering = ('sku',)
# Sort ordering stock keeping unit, has to be a tuple, alternatively (-'sku')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
