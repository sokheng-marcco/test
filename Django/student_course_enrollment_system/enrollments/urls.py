from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('add/', views.enrollment_add, name='enrollment_add'),
    path('edit/<int:pk>/', views.enrollment_edit, name='enrollment_edit'),
    path('delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
]