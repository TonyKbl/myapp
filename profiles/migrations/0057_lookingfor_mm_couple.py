# Generated by Django 5.0.6 on 2024-10-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0056_alter_profile_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookingfor',
            name='mm_couple',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
