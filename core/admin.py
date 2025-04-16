from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem

# Register your models here.
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag'] # this will add a search bar to the tag field
    model = TaggedItem
    extra = 0

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline] # this will add the TagInline to the ProductAdmin

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)