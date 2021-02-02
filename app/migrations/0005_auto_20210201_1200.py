# Generated by Django 3.1.2 on 2021-02-01 06:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20210201_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 12, 0, 13, 936364)),
        ),
        migrations.AlterField(
            model_name='like',
            name='discuss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.discussion'),
        ),
        migrations.AlterField(
            model_name='like',
            name='userlikes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 12, 0, 13, 936364)),
        ),
    ]
