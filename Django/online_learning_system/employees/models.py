from django.db import models
from django.contrib.auth.models import make_password

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Automatically hash password if not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
