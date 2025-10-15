from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def teacher_add(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'teachers/teacher_form.html', {'form': form})

def teacher_edit(request, pk):
    teacher = Teacher.objects.filter(pk=pk).first()
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'teachers/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = Teacher.objects.filter(pk=pk).first()
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teachers/teacher_delete.html', {'teacher': teacher})    

