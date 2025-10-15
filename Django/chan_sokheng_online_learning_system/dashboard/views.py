from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Count
from students.models import Student
from instructors.models import Instructor
from employees.models import Employee
from enrollments.models import Enrollment
from lessons.models import Lesson
from assignments.models import Assignment
from submissions.models import Submission
from courses.models import Course, Review
from employees.decorators import employee_login_required

@employee_login_required
def dashboard_home(request):
    total_students = Student.objects.count()
    total_instructors = Instructor.objects.count()
    total_employees = Employee.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()
    published_courses = Course.objects.filter(published=True).count()

    context = {
        'total_students': total_students,
        'total_instructors': total_instructors,
        'total_employees': total_employees,
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'published_courses': published_courses,
    }
    return render(request, 'dashboard/home.html', context)


