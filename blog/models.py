import uuid

from django.db import models
from django.utils import timezone

from django.core.validators import FileExtensionValidator


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Page(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.UUIDField(max_length=30, unique=True, default=uuid.uuid4)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='pages')
    owner = models.ForeignKey('users.User',
                              on_delete=models.CASCADE,
                              related_name='pages')
    followers = models.ManyToManyField('users.User', related_name='follows', blank=True)
    image = models.URLField(null=True,
                            blank=True)
    image_file = models.ImageField(null=True,
                                   blank=True,
                                   validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    is_private = models.BooleanField(default=False)
    follow_requests = models.ManyToManyField('users.User',
                                             related_name='requests',
                                             blank=True)
    time_before_unban = models.DateTimeField(default=timezone.now, blank=True)
    is_blocked = models.BooleanField(default=False)


class Post(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=100)
    reply_to = models.ForeignKey('blog.Post', on_delete=models.SET_NULL, null=True, related_name='replies', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
