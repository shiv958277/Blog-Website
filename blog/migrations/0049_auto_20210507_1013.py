# Generated by Django 3.0.8 on 2021-05-07 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_registration_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='im',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='ima',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
