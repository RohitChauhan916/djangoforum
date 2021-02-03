# Generated by Django 3.1.2 on 2020-11-19 07:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201119_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='profile_photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 12, 31, 9, 272725)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 12, 31, 9, 257063)),
        ),
    ]