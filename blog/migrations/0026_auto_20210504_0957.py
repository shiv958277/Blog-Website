# Generated by Django 3.0.8 on 2021-05-04 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Time_upload',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
