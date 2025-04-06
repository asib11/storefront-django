from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('product/<int:id>/', views.product_detail),
    # path('collection/', views.collection_list),
    path('collection/<int:pk>/', views.collection_detail, name='collection-detail'), # strandard naming convention is pk instad of id
]
