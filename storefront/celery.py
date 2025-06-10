import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')
celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
# celery -A storefront.celery worker -l info
# celery -A storefront.celery beat -l info
# celery -A storefront.celery flower
# celery -A storefront.celery shell
# celery -A storefront.celery call 'tasks.add' -l info