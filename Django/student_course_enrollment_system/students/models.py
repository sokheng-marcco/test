from django.db import models

class Student(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    address = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.name
    
    