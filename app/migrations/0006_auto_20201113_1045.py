# Generated by Django 3.1.2 on 2020-11-13 05:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201112_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 10, 45, 32, 72309)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 10, 45, 32, 72309)),
        ),
        migrations.CreateModel(
            name='userPhoto',
            fields=[
                ('up_id', models.AutoField(primary_key=True, serialize=False)),
                ('photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
    ]