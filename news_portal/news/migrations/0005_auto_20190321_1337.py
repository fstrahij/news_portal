# Generated by Django 2.1.7 on 2019-03-21 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='guid',
            new_name='rss',
        ),
    ]