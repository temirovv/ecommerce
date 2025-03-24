from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0, help_text="Foydalanuvchining Yoshi")

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = "Foydalanuvchilar"


class Profile(models.Model):
    image = models.ImageField(upload_to='users/')

    class Meta:
        abstract = True


class UserProfile(Profile):
    address = models.CharField(max_length=120)
    passport_number = models.CharField(max_length=6)
