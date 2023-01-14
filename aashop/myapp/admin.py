from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    list_display = ('name', 'price', 'time_creation', 'photo')
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
