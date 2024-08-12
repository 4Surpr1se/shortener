# Generated by Django 5.1 on 2024-08-09 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortedURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("short_url", models.CharField(max_length=6, unique=True)),
                (
                    "death_time",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 9, 8, 22, 58, 36, 950023)
                    ),
                ),
            ],
        ),
    ]
