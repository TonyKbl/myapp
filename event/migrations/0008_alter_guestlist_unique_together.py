# Generated by Django 5.0.6 on 2024-10-22 00:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_clubevent_image_alter_festival_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='guestlist',
            unique_together={('guest', 'event')},
        ),
    ]