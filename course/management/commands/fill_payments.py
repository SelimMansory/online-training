from django.core.management import BaseCommand
from course.models import Payments, Course
from users.models import User
import random


class Command(BaseCommand):

    method = ['наличные', 'перевод на счет']
    def handle(self, *args, **options):
        Payments.objects.create(
            user=User.objects.filter(email='admin@admin.admin').first(),
            payment_amount=1000.0,
            payment_method=random.choice(self.method),
            course=Course.objects.all().first()
        )