from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)

# Nested router
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carItem_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carItem_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + product_router.urls +carItem_router.urls

# # URLConf
# urlpatterns = [
#     path('products/', views.ProductList.as_view()), # class based view
#     path('products/<int:pk>/', views.ProductDetail.as_view()), # class based view
#     path('collections/', views.CollectionList.as_view()), # class based view
#     path('collections/<int:pk>/', views.CollectionDetails.as_view(), name='collection-detail'), # strandard naming convention is pk instad of id
# ]
