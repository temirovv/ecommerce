from django.contrib.admin import ModelAdmin, register
from .models import Category, Product, ProductImage, Color


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@register(ProductImage)
class ProductImageModelAdmin(ModelAdmin):
    pass


@register(Color)
class ColorModelAdmin(ModelAdmin):
    list_display = ['name', 'product']


@register(Product)
class ProductModelAdmin(ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'discount']
    list_filter = ['name', 'price', 'quantity']
    search_fields = ['name']
    list_editable = ['discount']
    search_help_text = 'Nom orqali qiduruv'
