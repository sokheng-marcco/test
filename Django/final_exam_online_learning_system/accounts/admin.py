from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Instructor, Employee

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )
    list_display = ['username', 'role', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_superuser']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Employee)