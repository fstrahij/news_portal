# Generated by Django 2.1.7 on 2019-03-19 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='lastBuildDate',
        ),
    ]
