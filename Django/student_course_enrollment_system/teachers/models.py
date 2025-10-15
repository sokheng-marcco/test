from django.db import models

class Teacher(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name

