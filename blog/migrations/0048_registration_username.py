# Generated by Django 3.0.8 on 2021-05-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20210506_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='UserName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
