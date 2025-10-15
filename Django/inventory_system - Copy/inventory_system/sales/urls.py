from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.create_order, name='order_create'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
]