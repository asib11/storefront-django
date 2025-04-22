from rest_framework import serializers
from django.db import transaction
from decimal import Decimal
from store.models import Cart, CartItem, Customer, Order, OrderItem, Product, Collection, ProductImage, Review
from .signals import order_created

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

class ProductImageSrializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)
    
    class Meta:
        model = ProductImage
        fields = ['id', 'image'] # image is the name of the field in the through model

# model serializer
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSrializer(many=True, read_only=True) # nested serializer
    class Meta:
        model = Product
        fields = ['id', 'title', 'description','slug', 'inventory', 'unit_price', 'price_with_tax', 'collection', 'images']

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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date','name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)
    
class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']
    
class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']  
    
    
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    def get_total_price(self, cart: Cart):
        return sum(item.quantity * item.product.unit_price for item in cart.items.all())

    class Meta:
        model = Cart
        fields = ['id','items', 'total_price']

class AddCartItemSericalizer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Product does not exist')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        
        return self.instance 
    
    class Meta:
        model = CartItem
        fields = ['id','product_id', 'quantity']

class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']

class OrderItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product','unit_price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'placed_at', 'payment_status', 'customer', 'items']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']

    def validate_payment_status(self, value):
        if value not in Order.PaymentStatus:
            raise serializers.ValidationError('Invalid payment status')
        return value

    def update(self, instance, validated_data):
        instance.payment_status = validated_data['payment_status']
        instance.save()
        return instance

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('Cart does not exist')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError('Cart is empty')
        return cart_id

    def save(self, **kwargs):
        with transaction.atomic(): #use transaction to rollback if any error occurs
            cart_id = self.validated_data['cart_id']
            customer = Customer.objects.get(user_id=self.context['user_id'])
            order = Order.objects.create(customer=customer)
            cart_item = CartItem.objects.select_related('product').filter(cart_id=cart_id)
            order_items = [OrderItem(order=order, product= item.product, unit_price = item.product.unit_price, quantity = item.quantity) for item in cart_item]
            OrderItem.objects.bulk_create(order_items)
            Cart.objects.filter(pk=cart_id).delete()

            order_created.send_robust(self.__class__, order=order)
            return order
        
