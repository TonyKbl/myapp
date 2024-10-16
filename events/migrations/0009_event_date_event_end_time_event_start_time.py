# Generated by Django 5.0.6 on 2024-09-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_rename_events_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default='1970-1-1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default='20:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default='03:00:00'),
            preserve_default=False,
        ),
    ]
