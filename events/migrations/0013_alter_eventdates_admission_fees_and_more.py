# Generated by Django 5.0.6 on 2024-09-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_remove_event_additional_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdates',
            name='admission_fees',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='eventdates',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='eventdates',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='eventdates',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
