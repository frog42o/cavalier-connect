# Generated by Django 5.1.1 on 2024-11-06 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0009_alter_user_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
    ]
