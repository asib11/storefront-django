from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

    

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='claulate_tax') #custom sericalizer method field
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all(), source='collection.id')
    # collection = serializers.StringRelatedField(queryset=Collection.objects.all())
    collection = CollectionSerializer() # nested serializer
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail',
        # lookup_field='id'
    )

    def claulate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
