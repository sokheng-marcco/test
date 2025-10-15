from django.db import models

class Course(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    course_id = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user.title