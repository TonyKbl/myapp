# Generated by Django 5.0.6 on 2024-10-21 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_event_admission_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masterevent',
            old_name='ot_mmcoouples',
            new_name='ot_mmcouples',
        ),
    ]
