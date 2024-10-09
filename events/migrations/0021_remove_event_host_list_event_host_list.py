# Generated by Django 5.0.6 on 2024-10-09 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_alter_event_host_list'),
        ('pages', '0028_alter_page_cover_image_alter_page_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='host_list',
        ),
        migrations.AddField(
            model_name='event',
            name='host_list',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.pagehost'),
        ),
    ]
