from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, verbose_name='تلفن')

    def __str__(self):
        return f'{self.username} {self.get_full_name()}'
