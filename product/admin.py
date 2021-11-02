from django.contrib import admin

from product.models import CategoryModel, ColorModel, SizeModel, ProductModel, ProductDetailModel


class ProductDetailModelAdmin(admin.StackedInline):
    model = ProductDetailModel

    def __str__(self):
        return self.model


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['parent_menu', 'name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['parent_menu', 'name']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['color', 'created_at']
    list_filter = ['color']
    search_fields = ['color']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['size', 'created_at']
    list_filter = ['size']
    search_fields = ['size']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'created_at']
    list_filter = ['category', 'in_stock', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['category', 'color', 'size']
    inlines = [ProductDetailModelAdmin]

    def __str__(self):
        return self.model

    class Meta:
        model = ProductModel


@admin.register(ProductDetailModel)
class ProductDetailModelAdmin(admin.ModelAdmin):
    pass
