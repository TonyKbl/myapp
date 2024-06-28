# Generated by Django 4.0 on 2024-06-23 21:36

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_profile_cover_image_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[600, 600], upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[600, 200], upload_to='profiles'),
        ),
    ]