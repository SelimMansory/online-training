# Generated by Django 4.2.5 on 2023-10-13 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_course_last_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='last_update',
        ),
    ]