from datetime import datetime

from celery import shared_task

from users.models import User
import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task
def checking_user_activity(*args, **kwargs):
    # Создаем интервал для повтора
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS,
    )

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
        interval=schedule,
        name='Checking activity',
        task='users.tasks.checking_user_activity',
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )

    users = User.objects.filter(is_active=True, is_superuser=False)

    for user in users:
        if user.last_login is not None and (datetime.now() - user.last_login).day > 30:
            user.is_active = False
            user.save()