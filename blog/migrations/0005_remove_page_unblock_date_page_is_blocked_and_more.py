# Generated by Django 4.1 on 2022-09-21 15:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='unblock_date',
        ),
        migrations.AddField(
            model_name='page',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='time_before_unban',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
