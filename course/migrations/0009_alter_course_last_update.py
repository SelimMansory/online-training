# Generated by Django 4.2.5 on 2023-10-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='последнее обновление'),
        ),
    ]