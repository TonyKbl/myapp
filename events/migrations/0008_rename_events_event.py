# Generated by Django 5.0.6 on 2024-09-05 00:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_events_location'),
        ('pages', '0015_alter_page_address1_alter_page_address2_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]