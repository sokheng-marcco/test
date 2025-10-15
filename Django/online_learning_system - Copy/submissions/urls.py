from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_list, name='submission_list'),
    path('create/', views.submission_create, name='submission_create'),
    path('update/<int:pk>/', views.submission_update, name='submission_update'),
    path('delete/<int:pk>/', views.submission_delete, name='submission_delete'),
]