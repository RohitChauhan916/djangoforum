# Generated by Django 3.1.2 on 2021-02-01 07:25

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20210201_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 12, 55, 47, 768542)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 12, 55, 47, 768542)),
        ),
    ]