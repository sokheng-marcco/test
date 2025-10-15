from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    username = models.CharField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == 'student' and not hasattr(self, 'student_profile'):
            Student.objects.create(user=self)
        elif self.role == 'instructor' and not hasattr(self, 'instructor_profile'):
            Instructor.objects.create(user=self)
        elif self.role == 'employee' and not hasattr(self, 'employee_profile'):
            Employee.objects.create(user=self)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return f"Student: {self.user.username}"

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    expertise = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Instructor: {self.user.username}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.CharField(max_length=100, blank=True)
    employee_id = models.CharField(max_length=50, unique=True, blank=True)
    
    def __str__(self):
        return f"Employee: {self.user.username}"