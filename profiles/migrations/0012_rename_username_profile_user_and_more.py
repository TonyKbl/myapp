# Generated by Django 4.0 on 2024-06-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_rename_user_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('', 'Select Profile Type'), ('M', 'Single Male'), ('F', 'Single Female'), ('F', 'CD_TV'), ('F', 'TV_TS'), ('MF', 'Couple MF'), ('SR', 'Couple FF')], default='', max_length=2),
        ),
    ]
