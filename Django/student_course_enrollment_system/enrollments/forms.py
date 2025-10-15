from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'completion_date']
        widgets = {
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
        }
        