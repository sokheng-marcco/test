from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import Course, Category, Tag, Enrollment, Lesson, Assignment, Submission, Review, LessonProgress
from .forms import ReviewForm, SubmissionForm

def course_list(request):
    courses = Course.objects.filter(published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    category_filter = request.GET.get('category')
    tag_filter = request.GET.get('tag')
    instructor_filter = request.GET.get('instructor')
    
    if category_filter:
        courses = courses.filter(category_id=category_filter)
    if tag_filter:
        courses = courses.filter(tags__id=tag_filter)
    if instructor_filter:
        courses = courses.filter(instructor_id=instructor_filter)
    
    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags,
        'selected_category': int(category_filter) if category_filter else None,
        'selected_tag': int(tag_filter) if tag_filter else None,
        'selected_instructor': int(instructor_filter) if instructor_filter else None,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id, published=True)
    lessons = course.lesson_set.all().order_by('order')
    reviews = course.review_set.filter(moderated=True).order_by('-created_date')
    
    is_enrolled = False
    enrollment = None
    if request.user.is_authenticated and request.user.role == 'student':
        try:
            enrollment = Enrollment.objects.get(student=request.user, course=course)
            is_enrolled = True
        except Enrollment.DoesNotExist:
            pass
    
    context = {
        'course': course,
        'lessons': lessons,
        'reviews': reviews,
        'is_enrolled': is_enrolled,
        'enrollment': enrollment,
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
def enroll_course(request, course_id):
    if request.user.role != 'student':
        return HttpResponseForbidden()
    
    course = get_object_or_404(Course, id=course_id, published=True)
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user, 
        course=course
    )
    
    if created:
        messages.success(request, f'Successfully enrolled in {course.title}!')
    else:
        messages.info(request, f'You are already enrolled in {course.title}.')
    
    return redirect('course_detail', course_id=course.id)

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    if request.user.role == 'student':
        try:
            enrollment = Enrollment.objects.get(student=request.user, course=lesson.course)
        except Enrollment.DoesNotExist:
            return HttpResponseForbidden("You must be enrolled in this course to view lessons.")
        
        progress, created = LessonProgress.objects.get_or_create(
            enrollment=enrollment,
            lesson=lesson,
            defaults={'completed': True, 'completed_date': timezone.now()}
        )
        if not progress.completed:
            progress.completed = True
            progress.completed_date = timezone.now()
            progress.save()
    
    assignments = lesson.assignment_set.all()
    
    context = {
        'lesson': lesson,
        'assignments': assignments,
    }
    return render(request, 'courses/lesson_detail.html', context)

@login_required
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    if request.user.role == 'student':
        try:
            Enrollment.objects.get(student=request.user, course=assignment.lesson.course)
        except Enrollment.DoesNotExist:
            return HttpResponseForbidden("You must be enrolled in this course.")
        
        try:
            submission = Submission.objects.get(assignment=assignment, student=request.user)
        except Submission.DoesNotExist:
            submission = None
        
        if request.method == 'POST' and not submission:
            form = SubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                submission = form.save(commit=False)
                submission.assignment = assignment
                submission.student = request.user
                submission.save()
                messages.success(request, 'Assignment submitted successfully!')
                return redirect('assignment_detail', assignment_id=assignment.id)
        else:
            form = SubmissionForm()
        
        context = {
            'assignment': assignment,
            'submission': submission,
            'form': form,
        }
    else:
        context = {'assignment': assignment}
    
    return render(request, 'courses/assignment_detail.html', context)

@login_required
def add_review(request, course_id):
    if request.user.role != 'student':
        return HttpResponseForbidden()
    
    course = get_object_or_404(Course, id=course_id)
    
    try:
        Enrollment.objects.get(student=request.user, course=course)
    except Enrollment.DoesNotExist:
        return HttpResponseForbidden("You must be enrolled in this course to leave a review.")
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review, created = Review.objects.get_or_create(
                course=course,
                student=request.user,
                defaults={
                    'rating': form.cleaned_data['rating'],
                    'comment': form.cleaned_data['comment']
                }
            )
            if not created:
                review.rating = form.cleaned_data['rating']
                review.comment = form.cleaned_data['comment']
                review.save()
            
            messages.success(request, 'Review submitted successfully!')
            return redirect('course_detail', course_id=course.id)
    else:
        form = ReviewForm()
    
    context = {
        'course': course,
        'form': form,
    }
    return render(request, 'courses/add_review.html', context)