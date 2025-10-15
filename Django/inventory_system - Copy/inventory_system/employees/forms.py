from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'phone', 'adress', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }