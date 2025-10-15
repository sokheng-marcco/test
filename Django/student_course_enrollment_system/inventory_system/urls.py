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
from students import urls as students_urls
from teachers import urls as teachers_urls
from courses import urls as courses_urls
from enrollments import urls as enrollments_urls
from dashboard import urls as dashboard_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include(students_urls)), 
    path('teachers/', include(teachers_urls)),
    path('courses/', include(courses_urls)),
    path('enrollments/', include(enrollments_urls)),
    # path('dashboard/', include(dashboard_urls)),
    # path('accounts/', include(accounts_urls)),
]
