from django.shortcuts import render, redirect
from .models import Instructor
from .forms import InstructorForm

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors/instructor_list.html', {'instructors': instructors})

def instructor_create(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    return render(request, 'instructors/instructor_form.html', {'form': form})

def instructor_update(request, pk):
    instructor = Instructor.objects.filter(pk=pk).first()
    form = InstructorForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    return render(request, 'instructors/instructor_form.html', {'form': form})

def instructor_delete(request, pk):
    instructor = Instructor.objects.filter(pk=pk).first()
    if request.method == 'POST':
        instructor.delete()
        return redirect('instructor_list')
    return render(request, 'instructors/instructor_delete.html', {'instructor': instructor})