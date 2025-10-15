from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('create/', views.lesson_create, name='lesson_create'), 
    path('update/<int:pk>/', views.lesson_update, name='lesson_update'),
    path('delete/<int:pk>/', views.lesson_delete, name='lesson_delete'),
]