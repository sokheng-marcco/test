"""
URL configuration for inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from students import urls as students_urls
from instructors import urls as instructors_urls
from employees import urls as employees_urls
from categories import urls as categories_urls
from tags import urls as tags_urls  
from courses import urls as courses_urls
from enrollments import urls as enrollments_urls
from lessons import urls as lessons_urls
from assignments import urls as assignments_urls
from submissions import urls as submissions_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include(students_urls)),
    path('instructors/', include(instructors_urls)),
    path('employees/', include(employees_urls)),
    path('categories/', include(categories_urls)),
    path('tags/', include(tags_urls)),
    path('courses/', include(courses_urls)),
    path('enrollments/', include(enrollments_urls)),
    path('lessons/', include(lessons_urls)),
    path('assignments/', include(assignments_urls)),
    path('submissions/', include(submissions_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)