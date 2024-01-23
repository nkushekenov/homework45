from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    fields = (('name', 'price',),'category')
    readonly_fields = ('category',)
    search_fields = ('name', 'price')
    list_display_links = ('category',)
    list_editable = ('name', 'price')
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)