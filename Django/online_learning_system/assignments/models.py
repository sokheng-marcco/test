from django.db import models
from lessons.models import Lesson

class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    max_score = models.PositiveIntegerField(default=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 