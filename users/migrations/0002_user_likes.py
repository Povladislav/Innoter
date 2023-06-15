# Generated by Django 4.1 on 2022-09-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_reply_to'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='liked_posts', to='blog.post'),
        ),
    ]
