# Generated by Django 3.1.2 on 2020-11-19 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201119_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 12, 31, 22, 554516)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 12, 31, 22, 554516)),
        ),
    ]
