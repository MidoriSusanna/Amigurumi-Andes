from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    """"To improve admin experiencea and display products in a certain way"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'size',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product)
admin.site.register(Category)

