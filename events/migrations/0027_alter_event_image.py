# Generated by Django 5.0.6 on 2024-10-14 01:43

import django_resized.forms
import events.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=events.models.PathAndRename('event_images/2024/10/14')),
        ),
    ]
