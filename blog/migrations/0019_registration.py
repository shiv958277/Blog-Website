# Generated by Django 3.0.8 on 2021-05-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0018_auto_20210503_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('FirstName', models.CharField(max_length=100, null=True)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Password', models.CharField(max_length=300)),
                ('ConfirmPassword', models.CharField(max_length=300)),
            ],
        ),
    ]
