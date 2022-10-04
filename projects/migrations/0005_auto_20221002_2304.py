# Generated by Django 2.2.14 on 2022-10-02 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20221002_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='time_left',
            new_name='ended_date',
        ),
        migrations.AddField(
            model_name='projects',
            name='started_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
