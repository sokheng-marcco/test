from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'completed', 'progress']
        widgets = {
            'completed': forms.CheckboxInput(),
            'progress': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }