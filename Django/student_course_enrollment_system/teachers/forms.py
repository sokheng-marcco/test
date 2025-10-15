from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'phone', 'subject']
        
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'phone': 'Phone Number',
            'subject': 'Subject',
        }