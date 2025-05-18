from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.helloView.as_view(), name='hello'),
]
