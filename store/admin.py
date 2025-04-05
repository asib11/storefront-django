from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib.admin import SimpleListFilter
from . import models

# custom filter
class InventoryFilter(SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>10', 'OK')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        if self.value() == '>10':
            return queryset.filter(inventory__gte=10)
        # return queryset

# Register your models here.
@admin.register(models.Product) # decorator is the best way to register models
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    

    def collection_title(self, product):
        return product.collection.title
    collection_title.short_description = 'Collection' # optional- this is the name that will be displayed in the admin panel

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    @admin.action(description='Clear inventory') #customize the action name
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f'{updated_count} products updated')

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith'] # __istartswith is case insensitive

    @admin.display(ordering='order_count')
    def order_count(self, customer):
        url = reverse('admin:store_order_changelist')+ '?'+ urlencode({
            'customer__id': str(customer.id)
        })
        return format_html('<a href={}>{}<a/>',url,customer.order_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count=Count('order')
        )
    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    # ordering = ['-placed_at']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    list_per_page = 10
    ordering = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse('admin:store_product_changelist')+ '?'+ urlencode({
            'collection__id': str(collection.id)
        })
        return format_html('<a href={}>{}<a/>',url,collection.products_count)


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
