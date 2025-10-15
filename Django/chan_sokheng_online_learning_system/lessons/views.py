from django.shortcuts import render, redirect
from lessons.models import Lesson
from lessons.forms import LessonForm

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_create(request):
    form = LessonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lesson_list')
    return render(request, 'lessons/lesson_form.html', {'form': form})

def lesson_update(request, pk):
    lesson = Lesson.objects.filter(pk=pk).first()
    form = LessonForm(request.POST or None, request.FILES or None , instance=lesson)
    if form.is_valid():
        form.save()
        return redirect('lesson_list')
    return render(request, 'lessons/lesson_form.html', {'form': form})

def lesson_delete(request, pk):
    lesson = Lesson.objects.filter(pk=pk).first()
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    return render(request, 'lessons/lesson_delete.html', {'lesson': lesson})