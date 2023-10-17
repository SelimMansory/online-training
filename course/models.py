import datetime

from django.conf import settings
from django.db import models

from course.validators import URLValidator
from users.models import NULLABLE, User


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')

    last_update = models.CharField(max_length=50, default=datetime.datetime.now(), **NULLABLE,
                                   verbose_name='последнее обновление')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')

    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(max_length=200, verbose_name='ссылка на видео')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')

    date_of_payment = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    payment_amount = models.FloatField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=30, verbose_name='способ оплаты')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок')

    def __str__(self):
        return f'{self.date_of_payment}, {self.payment_amount}, {self.payment_method}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'