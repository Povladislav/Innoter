# Generated by Django 4.1 on 2022-09-21 11:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_time_before_unban'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time_before_unban',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
