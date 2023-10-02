from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    role = [
        ('user', 'user'),
        ('staff', 'staff'),
    ]

    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=11, **NULLABLE, verbose_name='телефон')
    city = models.CharField(max_length=30, **NULLABLE, verbose_name='город')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватар')
    group = models.CharField(max_length=5, choices=role, verbose_name='группа', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []