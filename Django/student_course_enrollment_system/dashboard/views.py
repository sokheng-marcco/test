from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse

@login_required
def dashboard_redirect(request):
    role = request.user.role
    if role == 'student':
        return redirect('student_dashboard')
    elif role == 'teacher':
        return redirect('teacher_dashboard')
    elif role == 'courese':
        return redirect('courese_dashboard')
    return HttpResponse("Role not recognized.")

@login_required
def student_dashboard(request):
    return HttpResponse("Welcome to Student Dashboard")

@login_required
def teacher_dashboard(request):
    return HttpResponse("Welcome to Teacher Dashboard")

@login_required
def courese_dashboard(request):
    return HttpResponse("Welcome to Courese Dashboard")
