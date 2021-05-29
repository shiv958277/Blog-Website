# Generated by Django 3.0.8 on 2021-05-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Title', models.CharField(max_length=100, null=True)),
                ('Overview', models.CharField(max_length=1000, null=True)),
                ('Time_upload', models.DateTimeField(auto_now=True)),
                ('Author', models.CharField(max_length=100, null=True)),
                ('Email', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Category', models.CharField(max_length=100, null=True)),
                ('Thumbnail', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]