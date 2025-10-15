from django.db import models
from courses.models import Course
from django.contrib.auth import get_user_model

User = get_user_model()

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True)
    document = models.FileField(upload_to='lesson_documents/', blank=True, null=True)
    order = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title