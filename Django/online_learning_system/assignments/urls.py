from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('create/', views.assignment_create, name='assignment_create'),
    path('update/<int:pk>/', views.assignment_update, name='assignment_update'),
    path('delete/<int:pk>/', views.assignment_delete, name='assignment_delete'),
]