# Generated by Django 3.0.8 on 2021-05-04 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='lkes',
        ),
    ]
