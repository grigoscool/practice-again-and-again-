from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    list_display = ('name', 'price', 'time_creation', 'photo')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', )

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
