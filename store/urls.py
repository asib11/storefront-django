from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view()), # class based view
    path('products/<int:pk>/', views.ProductDetail.as_view()), # class based view
    path('collections/', views.CollectionList.as_view()), # class based view
    path('collections/<int:pk>/', views.CollectionDetails.as_view(), name='collection-detail'), # strandard naming convention is pk instad of id
]
