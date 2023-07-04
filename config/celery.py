import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_work.settings')

app = Celery(
    'backend',
    broker = 'amqp://guest:guest@localhost:5672//'
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = 'amqp://guest:guest@localhost:5672//'

app.conf.timezone = 'Europe/Moscow'

app.autodiscover_tasks()
