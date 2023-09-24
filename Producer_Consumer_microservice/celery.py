from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

from Producer_Consumer_microservice.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Producer_Consumer_microservice.settings')

app = Celery('Producer_Consumer_microservice', broker=CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'order_creation': {
        'task': 'order.tasks.order_creation',
        'schedule': crontab(minute='*/1'),
    }
}
