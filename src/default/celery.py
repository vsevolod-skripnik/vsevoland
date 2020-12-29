import os

from celery import Celery
from django.conf import settings

__all__ = ['celery']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'default.settings')

celery = Celery('default')
celery.config_from_object(settings)
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
