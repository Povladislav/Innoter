from celery import shared_task

from .models import User


@shared_task
def sample_task():
    return "Hello world"


@shared_task
def unban_user_task():
    users = User.objects.filter(bantime__gt=0)
    for user in users:
        user.bantime -= 1
        if user.bantime == 0:
            user.is_blocked = False
        user.save()
