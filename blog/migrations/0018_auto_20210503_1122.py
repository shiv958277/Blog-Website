# Generated by Django 3.0.8 on 2021-05-03 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
