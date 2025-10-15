from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username


