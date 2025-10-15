from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'age', 'phone', 'address', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }