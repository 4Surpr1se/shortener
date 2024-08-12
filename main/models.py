from datetime import datetime, timedelta
from django.db import models
from main.static import DAYS_URL_LIVES, SHORT_URL_LENGTH
import django_rq


class ShortedURL(models.Model):
    url = models.URLField()
    short_url = models.CharField(unique=True, max_length=SHORT_URL_LENGTH)  # todo validation
    death_time = models.DateTimeField(default=datetime.now() + timedelta(days=DAYS_URL_LIVES))
