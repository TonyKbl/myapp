# Generated by Django 5.0.6 on 2024-09-30 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place_area', '0007_rename_postcode_outerpostcode_outer_pc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outerpostcode',
            old_name='outer_pc',
            new_name='postcode',
        ),
    ]