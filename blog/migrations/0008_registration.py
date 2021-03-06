# Generated by Django 3.0.8 on 2021-05-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Password', models.CharField(max_length=300)),
                ('ConfirmPassword', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]
