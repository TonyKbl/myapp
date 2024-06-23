# Generated by Django 4.0 on 2024-06-23 16:16

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_profile_description_profile_headline_profile_intro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_image',
            field=django_resized.forms.ResizedImageField(crop=None, default=1, force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 500], upload_to='profiles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[200, 500], upload_to='profiles'),
        ),
    ]