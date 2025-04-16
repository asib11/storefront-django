from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag'] # this will add a search bar to the tag field
    model = TaggedItem
    extra = 0

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline] # this will add the TagInline to the ProductAdmin

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)