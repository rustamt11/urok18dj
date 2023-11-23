# customer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('buy_product/<int:id>/', views.buy_product, name='buy_product'),
]
