# Generated by Django 5.1.1 on 2024-10-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
