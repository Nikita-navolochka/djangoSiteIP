from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'author', 'grade', 'part']
    list_filter = ['category', 'grade', 'author', 'part']
    search_fields = ['name', 'grade', 'author', 'part', 'category']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',  'slug']
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
