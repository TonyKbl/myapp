# Generated by Django 5.0.6 on 2024-10-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_alter_event_admission_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='admission_fees',
            field=models.TextField(default='\nCouples £\nSingle Males    £\nSingle Females  £\nTV/TS   £', null=True),
        ),
    ]
