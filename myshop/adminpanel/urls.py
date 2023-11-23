# adminpanel/urls.py
from django.urls import path

from adminpanel import views


urlpatterns = [
    path('start_page/', views.admin_product_list, name='admin_product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
]
