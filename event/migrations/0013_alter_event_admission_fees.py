# Generated by Django 5.0.6 on 2024-10-28 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_alter_clubevent_image_alter_festival_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='admission_fees',
            field=models.TextField(default='\n    Couples\t£\n    Single Males\t£\n    Single Females\t£\n    TV/TS\t£', null=True),
        ),
    ]
