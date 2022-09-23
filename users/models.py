from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField(unique=True)
    image_localstack_path = models.URLField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=9, choices=Roles.choices, default=Roles.USER)
    title = models.CharField(max_length=80)
    likes = models.ManyToManyField('blog.Post', related_name="liked_posts", blank=True)
    time_before_unban = models.DateTimeField(default=timezone.now, blank=True)
    is_blocked = models.BooleanField(default=False)
