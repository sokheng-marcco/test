from django.shortcuts import render, redirect
from assignments.models import Assignment
from assignments.forms import AssignmentForm

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

def assignment_create(request):
    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('assignment_list')
    return render(request, 'assignments/assignment_form.html', {'form': form})

def assignment_update(request, pk):
    assignment = Assignment.objects.filter(pk=pk).first()
    form = AssignmentForm(request.POST or None, instance=assignment)
    if form.is_valid():
        form.save()
        return redirect('assignment_list')
    return render(request, 'assignments/assignment_form.html', {'form': form})

def assignment_delete(request, pk):
    assignment = Assignment.objects.filter(pk=pk).first()
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'assignments/assignment_delete.html', {'assignment': assignment})