from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product) # decorator is the best way to register models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory', 'collection']
    list_editable = ['unit_price', 'inventory']
    list_per_page = 10

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']

admin.site.register([
    models.Collection,
    # models.Customer,
    # models.Order,
    # models.Product,
    # models.Promotion
])
