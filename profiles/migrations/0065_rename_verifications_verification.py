# Generated by Django 5.0.6 on 2024-11-09 07:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0064_alter_verifications_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Verifications',
            new_name='Verification',
        ),
    ]