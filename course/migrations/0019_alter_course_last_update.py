# Generated by Django 4.2.7 on 2023-11-21 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_alter_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 11, 21, 19, 40, 28, 191090), max_length=50, null=True, verbose_name='последнее обновление'),
        ),
    ]
