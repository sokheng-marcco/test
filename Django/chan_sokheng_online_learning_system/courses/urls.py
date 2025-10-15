from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('update/<int:pk>/', views.course_update, name='course_update'),
    path('delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('review/list/<int:course_id>/', views.review_list, name='review_list'),
    path('review/create/<int:course_id>/', views.review_create, name='review_create'),
    path('review/update/<int:pk>/', views.review_update, name='review_update'),
    path('review/delete/<int:pk>/', views.review_delete, name='review_delete'),
]