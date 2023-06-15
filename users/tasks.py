from celery import shared_task
from django.utils import timezone

from .models import User


@shared_task
def sample_task():
    return "Hello world"


@shared_task
def unban_user_task():
    users = User.objects.filter(time_before_unban__lte=timezone.now())
    for user in users:
        user.is_blocked = False
        user.save()
