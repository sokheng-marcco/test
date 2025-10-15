from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_create(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_form.html', {'form': form})

def course_update(request, pk):
    course = Course.objects.filter(pk=pk).first()
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_form.html', {'form': form})

def course_delete(request, pk):
    course = Course.objects.filter(pk=pk).first()
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_delete.html', {'course': course})