# Generated by Django 5.0.6 on 2024-10-06 15:47

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_alter_page_lat_alter_page_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='loc',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
