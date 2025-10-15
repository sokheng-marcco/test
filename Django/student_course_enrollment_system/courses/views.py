from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_add(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_form.html', {'form': form})

def course_edit(request, pk):
    course = Course.objects.filter(pk=pk).first()
    if not course:
        return HttpResponse("Course not found", status=404)
    
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_form.html', {'form': form})

def course_delete(request, pk):
    course = Course.objects.filter(pk=pk).first()
    if not course:
        return HttpResponse("Course not found", status=404)
    
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_delete.html', {'course': course})
