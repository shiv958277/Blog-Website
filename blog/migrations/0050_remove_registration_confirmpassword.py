# Generated by Django 3.0.8 on 2021-05-10 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_auto_20210507_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='ConfirmPassword',
        ),
    ]
