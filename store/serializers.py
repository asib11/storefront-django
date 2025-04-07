from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

# model serializer
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True) # read only field

# normal serializer
# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


# model serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description','slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='claulate_tax') #custom sericalizer method
    
    def claulate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    # collection = serializers.HyperlinkedRelatedField(  # collection = CollectionSerializer() # nested serializer
    # queryset=Collection.objects.all(),
    # view_name='collection-detail',
    # )
  

#normal serializer
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(method_name='claulate_tax') #custom sericalizer method field
#     # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all(), source='collection.id')
#     # collection = serializers.StringRelatedField(queryset=Collection.objects.all())
#     collection = CollectionSerializer() # nested serializer
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name='collection-detail',

#     )

#     def claulate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)
