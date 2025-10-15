from django.shortcuts import render, redirect
from .models import Course, Review
from .forms import CourseForm, ReviewForm


# Course views.
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

# Review views.
def review_list(request, course_id):
    course = Course.objects.get(id=course_id)
    reviews = Review.objects.filter(course=course, moderated=True)
    return render(request, 'courses/review_list.html', {'course': course, 'reviews': reviews})

def review_create(request, course_id):
    course = Course.objects.get(id=course_id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.course = course
        review.student = request.user.student  # Assuming user is logged in and has a Student profile
        review.save()
        return redirect('course_detail', pk=course.id)
    return render(request, 'courses/review_form.html', {'form': form, 'course': course})

def review_update(request, pk):
    review = Review.objects.filter(pk=pk).first()
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('course_detail', pk=review.course.id)
    return render(request, 'courses/review_form.html', {'form': form, 'review': review})

def review_delete(request, pk):
    review = Review.objects.filter(pk=pk).first()
    if request.method == 'POST':
        course_id = review.course.id
        review.delete()
        return redirect('course_detail', pk=course_id)
    return render(request, 'courses/review_delete.html', {'review': review})