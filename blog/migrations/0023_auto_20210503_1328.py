# Generated by Django 3.0.8 on 2021-05-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210503_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Time_upload',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]