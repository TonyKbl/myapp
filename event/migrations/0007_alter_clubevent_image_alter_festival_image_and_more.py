# Generated by Django 5.0.6 on 2024-10-21 23:52

import django.db.models.deletion
import django_resized.forms
import event.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_eventhost'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubevent',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/22')),
        ),
        migrations.AlterField(
            model_name='festival',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/22')),
        ),
        migrations.AlterField(
            model_name='privateparty',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/22')),
        ),
        migrations.AlterField(
            model_name='social',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/22')),
        ),
        migrations.CreateModel(
            name='Guestlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
