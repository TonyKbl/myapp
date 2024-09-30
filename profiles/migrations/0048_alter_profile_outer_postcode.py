# Generated by Django 5.0.6 on 2024-09-30 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place_area', '0007_rename_postcode_outerpostcode_outer_pc'),
        ('profiles', '0047_profile_lat_profile_lon_profile_outer_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='outer_postcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place_area.outerpostcode'),
        ),
    ]