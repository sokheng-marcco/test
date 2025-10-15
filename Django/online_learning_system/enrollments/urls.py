from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('create/', views.enrollment_create, name='enrollment_create'),
    path('update/<int:pk>/', views.enrollment_update, name='enrollment_update'),
    path('delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
]
