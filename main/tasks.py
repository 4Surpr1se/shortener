from datetime import datetime

from celery import shared_task

from main.models import ShortedURL


@shared_task
def delete_expired_short_urls():
    ShortedURL.objects.filter(death_time__lte=datetime.now()).delete()
