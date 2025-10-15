from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_list, name='instructor_list'),
    path('create/', views.instructor_create, name='instructor_create'),
    path('update/<int:pk>/', views.instructor_update, name='instructor_update'),
    path('delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
]