# Generated by Django 5.0.6 on 2024-08-18 13:46

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_page_page_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 200], upload_to='page_covers'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to='page_avatars'),
        ),
    ]