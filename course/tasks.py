from celery import shared_task
from django.core.mail import send_mail
from config import settings
from subscribe.models import SubscribeUser


@shared_task
def send_an_update_mail(course):
    """
    Рассылка писем об обновления курса
    """
    subscribes = SubscribeUser.objects.filter(course=course, subscribe=True)
    for subscribe in subscribes:
        send_mail(
            'Обновление курса!',
            f'Курс {subscribe.course.title} получил обновление!',
            settings.EMAIL_HOST_USER,
            [subscribe.user.email]
        )