# Generated by Django 5.0.6 on 2024-09-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_events_description_alter_events_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='private',
            field=models.BooleanField(default=0),
        ),
    ]