from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')
app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send-overdue-task-emails-daily': {
        'task': 'task_manager_app.tasks.sendOverdueTaskEmails',
        'schedule': crontab(minute='*/1'),
        # 'schedule': crontab(hours='*/12'),
        # 'args' : (2, )
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')