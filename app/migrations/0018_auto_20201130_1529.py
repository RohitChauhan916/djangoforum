# Generated by Django 3.1.2 on 2020-11-30 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20201130_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 15, 29, 37, 107746)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 15, 29, 37, 107746)),
        ),
    ]