# Generated by Django 5.0.6 on 2024-09-27 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0042_alter_level_level_alter_level_level_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlevel',
            name='level',
            field=models.OneToOneField(default=10, on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.level'),
        ),
    ]
