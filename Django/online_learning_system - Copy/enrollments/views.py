from django.shortcuts import render, redirect
from enrollments.models import Enrollment
from enrollments.forms import EnrollmentForm    

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

def enrollment_create(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_form.html', {'form': form})

def enrollment_update(request, pk):
    enrollment = Enrollment.objects.filter(pk=pk).first()
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_form.html', {'form': form})

def enrollment_delete(request, pk):
    enrollment = Enrollment.objects.filter(pk=pk).first()
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_delete.html', {'enrollment': enrollment})