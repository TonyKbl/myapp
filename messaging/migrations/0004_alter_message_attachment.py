# Generated by Django 5.0.6 on 2024-09-11 00:23

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_message_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='attachment',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[600, 200], upload_to='message_attachments'),
        ),
    ]
