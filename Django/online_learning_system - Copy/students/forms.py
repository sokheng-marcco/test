from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'phone', 'address', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }