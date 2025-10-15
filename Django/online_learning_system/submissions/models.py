from django.db import models
from django.core.validators import MaxValueValidator
from students.models import Student
from assignments.models import Assignment

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file_submission = models.FileField(upload_to='submissions/', blank=True, null=True)
    text_submission = models.TextField(blank=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(100)])
    feedback = models.TextField(blank=True)
    graded = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('assignment', 'student')
    
    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"