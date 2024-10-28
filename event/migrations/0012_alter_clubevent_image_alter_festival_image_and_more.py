# Generated by Django 5.0.6 on 2024-10-25 00:30

import django_resized.forms
import event.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_alter_clubevent_image_alter_festival_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubevent',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/')),
        ),
        migrations.AlterField(
            model_name='festival',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/')),
        ),
        migrations.AlterField(
            model_name='privateparty',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/')),
        ),
        migrations.AlterField(
            model_name='social',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/')),
        ),
    ]
