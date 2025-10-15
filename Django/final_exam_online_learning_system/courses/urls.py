from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('course/<int:course_id>/review/', views.add_review, name='add_review'),
]