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

def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related('course')
    upcoming_assignments = Assignment.objects.filter(
        lesson__course__in=[e.course for e in enrollments],
        due_date__gte=timezone.now()
    ).order_by('due_date')[:5]
    
    recent_submissions = Submission.objects.filter(
        student=request.user,
        graded=True
    ).order_by('-submitted_date')[:5]
    
    context = {
        'enrollments': enrollments,
        'upcoming_assignments': upcoming_assignments,
        'recent_submissions': recent_submissions,
    }
    return render(request, 'dashboard/student_dashboard.html', context)

def instructor_dashboard(request):
    my_courses = Course.objects.filter(instructor=request.user).annotate(
        enrollment_count=Count('enrollment_set')
    )
    
    pending_submissions = Submission.objects.filter(
        assignment__lesson__course__instructor=request.user,
        graded=False
    ).select_related('assignment', 'student')
    
    recent_reviews = Review.objects.filter(
        course__instructor=request.user
    ).order_by('-created_date')[:5]
    
    context = {
        'my_courses': my_courses,
        'pending_submissions': pending_submissions,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'dashboard/instructor_dashboard.html', context)


def employee_dashboard(request):
    stats = {
        'total_students': Student.objects.filter(role='student').count(),
        'total_instructors': Instructor.objects.filter(role='instructor').count(),
        'total_courses': Course.objects.count(),
        'published_courses': Course.objects.filter(published=True).count(),
        'total_enrollments': Enrollment.objects.count(),
    }
    
    recent_enrollments = Enrollment.objects.order_by('-enrolled_date')[:10]
    recent_courses = Course.objects.order_by('-created_date')[:5]
    
    context = {
        'stats': stats,
        'recent_enrollments': recent_enrollments,
        'recent_courses': recent_courses,
    }
    return render(request, 'dashboard/employee_dashboard.html', context)