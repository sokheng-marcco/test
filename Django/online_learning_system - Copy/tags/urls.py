from django.urls import path
from . import views

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('create/', views.tag_create, name='tag_create'),
    path('update/<int:pk>/', views.tag_update, name='tag_update'),
    path('delete/<int:pk>/', views.tag_delete, name='tag_delete'),
]


