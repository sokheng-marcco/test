from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment', 'student', 'file_submission', 'text_submission', 'score', 'feedback', 'graded']