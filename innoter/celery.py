import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "innoter.settings")

app = Celery("innoter")
app.conf.update(timezone='Europe/Minsk')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
