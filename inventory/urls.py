from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_summary, name='inventory_summary'),  # Add this line
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_create, name='transaction_create'),
    path('inventory/', views.inventory_summary, name='inventory_summary'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
]