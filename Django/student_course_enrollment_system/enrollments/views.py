from django.shortcuts import render, redirect, HttpResponse
from .models import Enrollment
from .forms import EnrollmentForm

def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

def enrollment_add(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_form.html', {'form': form})

def enrollment_edit(request, pk):
    enrollment = Enrollment.objects.filter(pk=pk).first()
    if not enrollment:
        return HttpResponse("Enrollment not found", status=404)
    
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_form.html', {'form': form})

def enrollment_delete(request, pk): 
    enrollment = Enrollment.objects.filter(pk=pk).first()
    if not enrollment:
        return HttpResponse("Enrollment not found", status=404)
    
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_delete.html', {'enrollment': enrollment})    


