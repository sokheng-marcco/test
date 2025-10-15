from django.contrib import admin
from .models import Category, Tag, Course, Enrollment, Lesson, Assignment, Submission, Review, LessonProgress

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'category', 'price', 'published', 'created_date']
    list_filter = ['published', 'category', 'created_date']
    search_fields = ['title', 'description']
    filter_horizontal = ['tags']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrolled_date', 'completed', 'progress']
    list_filter = ['completed', 'enrolled_date']
    search_fields = ['student__username', 'course__title']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'created_date']
    list_filter = ['course', 'created_date']
    search_fields = ['title', 'description']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson', 'due_date', 'max_score', 'created_date']
    list_filter = ['due_date', 'created_date']
    search_fields = ['title', 'description']

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submitted_date', 'score', 'graded']
    list_filter = ['graded', 'submitted_date']
    search_fields = ['assignment__title', 'student__username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'rating', 'moderated', 'created_date']
    list_filter = ['rating', 'moderated', 'created_date']
    search_fields = ['course__title', 'student__username']

admin.site.register(LessonProgress)