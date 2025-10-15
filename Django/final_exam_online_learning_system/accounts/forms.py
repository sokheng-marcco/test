from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class StudentRegisterForm(CustomUserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if commit:
            user.save()
        return user


class InstructorRegisterForm(CustomUserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'instructor'
        if commit:
            user.save()
        return user


class EmployeeRegisterForm(CustomUserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employee'
        if commit:
            user.save()
        return user
