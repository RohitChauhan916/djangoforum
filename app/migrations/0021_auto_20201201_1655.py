# Generated by Django 3.1.2 on 2020-12-01 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20201201_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='departmant',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='name',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='reporting_to',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='zone',
        ),
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 16, 55, 5, 809201)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 16, 55, 5, 809201)),
        ),
    ]
