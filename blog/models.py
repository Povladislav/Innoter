from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Page(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.UUIDField(max_length=30, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='pages')
    owner = models.ForeignKey('users.User',
                              on_delete=models.CASCADE,
                              related_name='pages')
    followers = models.ManyToManyField('users.User', related_name='follows')
    image = models.URLField(null=True,
                            blank=True)
    is_private = models.BooleanField(default=False)
    follow_requests = models.ManyToManyField('users.User',
                                             related_name='requests')
    unblock_date = models.DateField(null=True, blank=True)


class Post(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=100)
    reply_to = models.ForeignKey('blog.Post', on_delete=models.SET_NULL, null=True, related_name='replies')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
