from django.contrib import admin

from pages.models import HomeModel, PopularModel, ServicesModel


@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'banner', 'created_at']
    list_filter = ['created_at', 'title']
    search_fields = ['created_at', 'title']


@admin.register(PopularModel)
class PopCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'created_at']
    list_filter = ['created_at', 'name', 'image']
    search_fields = ['created_at', 'name']


@admin.register(ServicesModel)
class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', ]
    list_filter = ['created_at', 'title']
    search_fields = ['created_at', 'title']