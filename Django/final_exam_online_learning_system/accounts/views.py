from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Avg
from courses.models import Course, Enrollment, Assignment, Submission, Review
from django.utils import timezone
from .forms import StudentRegisterForm, InstructorRegisterForm, EmployeeRegisterForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'instructor':
                return redirect('instructor_dashboard')
            elif user.role == 'employee':
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return redirect('login')
    
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
    return render(request, 'accounts/student_dashboard.html', context)

@login_required
def instructor_dashboard(request):
    if request.user.role != 'instructor':
        return redirect('login')
    
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
    return render(request, 'accounts/instructor_dashboard.html', context)

@login_required
def employee_dashboard(request):
    if request.user.role != 'employee':
        return redirect('login')
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    stats = {
        'total_users': User.objects.count(),
        'total_students': User.objects.filter(role='student').count(),
        'total_instructors': User.objects.filter(role='instructor').count(),
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
    return render(request, 'accounts/employee_dashboard.html', context)

def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or a dashboard
    else:
        form = StudentRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'title': 'Student Registration'})


def register_instructor(request):
    if request.method == 'POST':
        form = InstructorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = InstructorRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'title': 'Instructor Registration'})


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'title': 'Employee Registration'})