from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'address', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'grade': 'Grade Level',
            'address': 'Address',
            'date_of_birth': 'Date of Birth',
        }